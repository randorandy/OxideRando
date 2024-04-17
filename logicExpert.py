from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places.
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    GravitySuit, Varia, Wave, SpeedBooster, Spazer, Ice, Grapple,
    Plasma, Screw, Charge, SpaceJump, Energy, Reserve, Xray
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy)  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy)  >= 14
))


hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun2 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy300 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun6 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy700 in loadout)
))
hellrun8 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy900 in loadout)
))
hellrun9 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1000 in loadout)
))
hellrun11 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1200 in loadout)
))
hellrun14 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1500 in loadout)
))

missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 10
))
missile15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 15
))
super10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 5 >= 10
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 5 >= 30
))
powerBomb10 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb15 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
canCF = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (loadout.count(Items.PowerBomb) >= 3) and
    (super10 in loadout) and
    (missile10 in loadout)
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Missile in loadout) or
    (Super in loadout)
))

upper_crater = LogicShortcut(lambda loadout: (
    (Grapple in loadout) or
        (canIBJ in loadout) or
        (HiJump in loadout) or
        (SpeedBooster in loadout) or
        (SpaceJump in loadout) or
        (
            (Morph in loadout) and
            (Springball in loadout)
            )
))

maridia = LogicShortcut(lambda loadout: (
    (pinkDoor in loadout) and
    (Morph in loadout) and
    (canBreakBlocks in loadout)
    
))
phantoon = LogicShortcut(lambda loadout: (
    (maridia in loadout) and
    (Super in loadout) and
    (Ice in loadout) and
    (
        (canIBJ in loadout) or
        (SpaceJump in loadout) or
        (SpeedBooster in loadout) or
        (HiJump in loadout)
        )
))
middleship = LogicShortcut(lambda loadout: (
    (maridia in loadout) and
    (canUseBombs in loadout)
))
norfair = LogicShortcut(lambda loadout: (
    (middleship in loadout) and
    (Super in loadout)
))
ln = LogicShortcut(lambda loadout: (
    (norfair in loadout) and
    (
        (SpaceJump in loadout) or
        (canUsePB in loadout)
        )
))


allitems = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Missile in loadout) and
    (Super in loadout) and
    (PowerBomb in loadout) and
    (Springball in loadout) and
    (Bombs in loadout) and
    (HiJump in loadout) and
    (GravitySuit in loadout) and
    (Varia in loadout) and
    (Wave in loadout) and
    (SpeedBooster in loadout) and
    (Spazer in loadout) and
    (Ice in loadout) and
    (Grapple in loadout) and
    (Plasma in loadout) and
    (Screw in loadout) and
    (Charge in loadout) and
    (SpaceJump in loadout) and
    (Xray in loadout)
))


area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Grapple Beam": lambda loadout: (
        True
    ),
    "Springball": lambda loadout: (
        (upper_crater in loadout)
    ),
    "Missile": lambda loadout: (
        (upper_crater in loadout)
    ),
    "Morph Ball": lambda loadout: (
        (pinkDoor in loadout)
    ),
    "Bombs": lambda loadout: (
        (pinkDoor in loadout) and
        (Morph in loadout)
    ),
    "Alpha Super Missile": lambda loadout: (
        (maridia in loadout)
    ),
    "Charge Beam": lambda loadout: (
        (maridia in loadout)
    ),
    "Speed Room Energy": lambda loadout: (
        (maridia in loadout) and
        (Super in loadout)
    ),
    "Speed Booster": lambda loadout: (
        (maridia in loadout) and
        (Super in loadout)
    ),
    "WS Entry Energy": lambda loadout: (
        (maridia in loadout) and
        (Super in loadout)
    ),
    "WS Entry Speed Super": lambda loadout: (
        (maridia in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "WS Reserve Super": lambda loadout: (
        (phantoon in loadout)
    ),
    "WS Reserve": lambda loadout: (
        (phantoon in loadout)
    ),
    "Ice Beam": lambda loadout: (
        (phantoon in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout) or
            (super10 in loadout)
            )
    ),
    "WS Conveyor Energy": lambda loadout: (
        (phantoon in loadout)
    ),
    "WS Atomic Energy": lambda loadout: (
        (phantoon in loadout)
    ),
    "Gravity Suit": lambda loadout: (
        (phantoon in loadout)
    ),
    "Tourian Entry Reserve": lambda loadout: (
        (maridia in loadout)
    ),
    "Baby Skip Super": lambda loadout: (
        (middleship in loadout)
    ),
    "Longest Horizontal Energy": lambda loadout: (
        (middleship in loadout)
    ),
    "HiJump": lambda loadout: (
        (norfair in loadout) and
        (SpeedBooster in loadout)
    ),
    "GT Reserve Energy": lambda loadout: (
        (norfair in loadout)
    ),
    "GT Reserve Tank": lambda loadout: (
        (norfair in loadout)
    ),
    "Wave Super": lambda loadout: (
        (norfair in loadout) and
        (Wave in loadout)
    ),
    "Wave Beam": lambda loadout: (
        (norfair in loadout) and
        (Wave in loadout)
    ),
    "Grapple Ceiling Energy": lambda loadout: (
        (norfair in loadout) and
        (Wave in loadout) and
        (Grapple in loadout) and
        (
            (canIBJ in loadout) or
            (SpaceJump in loadout) or
            (
                (SpeedBooster in loadout) and
                (HiJump in loadout)
                ) #more?
            )
    ),
    "GT Super": lambda loadout: (
        (norfair in loadout)
    ),
    "GT Energy": lambda loadout: (
        (norfair in loadout)
    ),
    "GT Alpha Power Bomb": lambda loadout: (
        (norfair in loadout) and
        (
            (Wave in loadout) or
            (Spazer in loadout)
            )
    ),
    "Waterway Power Bomb": lambda loadout: (
        (norfair in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "Screw Attack": lambda loadout: (
        (norfair in loadout)
    ),
    "Brinstar Entry Speed Super": lambda loadout: (
        (norfair in loadout) and
        (SpeedBooster in loadout)
    ),
    "LN Elevator Energy": lambda loadout: (
        (norfair in loadout) and
        (canUsePB in loadout)
    ),
    "LN Cage Power Bomb": lambda loadout: (
        (ln in loadout) and
        (canUsePB in loadout) and
        (Varia in loadout) #hellrun
    ),
    "LN Hidden Floor Power Bomb": lambda loadout: (
        (ln in loadout) and
        (canUsePB in loadout) and
        (Varia in loadout) #hellrun
    ),
    "LN Ceiling Speedway Power Bomb": lambda loadout: (
        (ln in loadout) and
        (canUsePB in loadout) and
        (SpeedBooster in loadout) and
        (Varia in loadout) #hellrun
    ),
    "Ridley Energy Tank": lambda loadout: (
        (ln in loadout) and
        (canUsePB in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout)
            ) and
        (energy300 in loadout) and
        (Varia in loadout)
        
    ),
    "LN Pirate Wall Power Bomb": lambda loadout: (
        (ln in loadout) and
        (canUsePB in loadout) and
        (Varia in loadout) #hellrun
    ),
    "LN Reserve Tank": lambda loadout: (
        (ln in loadout) and
        (Varia in loadout) #hellrun
        
    ),
    "Spazer Energy": lambda loadout: (
        (middleship in loadout)
    ),
    "Spazer": lambda loadout: (
        (middleship in loadout)
    ),
    "Kraid Floor Super": lambda loadout: (
        (middleship in loadout)
    ),
    "Kraid Power Bomb": lambda loadout: (
        (middleship in loadout) and
        (canUsePB in loadout)
    ),
    "Varia Suit": lambda loadout: (
        (middleship in loadout) and
        (
            (canIBJ in loadout) or
            (HiJump in loadout) or
            (SpaceJump in loadout) or
            (SpeedBooster in loadout)
            )
    ),
    "X-ray Scope": lambda loadout: (
        (middleship in loadout) and
        (
            (canIBJ in loadout) or
            (HiJump in loadout) or
            (SpaceJump in loadout) or
            (SpeedBooster in loadout)
            )
    ),
    "Crater Energy Tank": lambda loadout: (
        (Morph in loadout) and
        (SpeedBooster in loadout) and
        (Springball in loadout)
    ),
    "Precious Energy": lambda loadout: (
        (maridia in loadout)
    ),
    "Precious Super": lambda loadout: (
        (maridia in loadout)
    ),
    "Space Jump": lambda loadout: (
        (maridia in loadout) and
        (
            (Charge in loadout) or
            (Missile in loadout) or
            (
                (SpeedBooster in loadout) and
                (Energy in loadout)
                )
            )
            
    ),
    "Triple Super Ceiling": lambda loadout: (
        (maridia in loadout) and
        (canUseBombs in loadout) and
        (
            (Charge in loadout) or
            (Missile in loadout) or
            (
                (SpeedBooster in loadout) and
                (Energy in loadout)
                )
            )
    ),
    "Triple Super Floor": lambda loadout: (
        (maridia in loadout) and
        (canUseBombs in loadout) and
        (
            (Charge in loadout) or
            (Missile in loadout) or
            (
                (SpeedBooster in loadout) and
                (Energy in loadout)
                )
            )
    ),
    "Triple Super Right": lambda loadout: (
        (maridia in loadout) and
        (canUseBombs in loadout) and
        (Super in loadout) and
        (
            (Charge in loadout) or
            (Missile in loadout) or
            (
                (SpeedBooster in loadout) and
                (Energy in loadout)
                )
            )
    ),
    "Triple Super Mid": lambda loadout: (
        (maridia in loadout) and
        (canUseBombs in loadout) and
        (Super in loadout) and
        (
            (Charge in loadout) or
            (Missile in loadout) or
            (
                (SpeedBooster in loadout) and
                (Energy in loadout)
                )
            )
    ),
    "Triple Super Left": lambda loadout: (
        (maridia in loadout) and
        (canUseBombs in loadout) and
        (Super in loadout) and
        (
            (Charge in loadout) or
            (Missile in loadout) or
            (
                (SpeedBooster in loadout) and
                (Energy in loadout)
                )
            )
    ),
    "Croc Super Missile": lambda loadout: (
        (allitems in loadout)
    ),
    "Plasma Beam": lambda loadout: (
        (allitems in loadout)
    ),
    "Escape Right Super": lambda loadout: (
        (allitems in loadout)
    ),
    "Escape Middle Super": lambda loadout: (
        (allitems in loadout)
    ),
    "Escape Left Super": lambda loadout: (
        (allitems in loadout)
    ),


}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
