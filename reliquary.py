import argparse
import pathlib
import typing

from utils import common
from utils import log


def get_template(icon_string: str) -> typing.List[str]:

    template = [
        "nanakpanthi_religion = {",
        "	family = rf_harmonic",
        "	graphical_faith = dharmic_gfx",
        "	",
        "	doctrine = harmonic_hostility_doctrine",
        "",
        "	#Main Group",
        "	doctrine = doctrine_no_head",
        "	doctrine = doctrine_gender_male_dominated",
        "	doctrine = doctrine_pluralism_pluralistic",
        "	doctrine = doctrine_theocracy_lay_clergy",
        "",
        "	#Marriage",
        "	doctrine = doctrine_monogamy",
        "	doctrine = doctrine_divorce_allowed",
        "	doctrine = doctrine_bastardry_legitimization",
        "	doctrine = doctrine_consanguinity_cousins",
        "",
        "	#Crimes",
        "	doctrine = doctrine_homosexuality_shunned",
        "	doctrine = doctrine_adultery_men_shunned",
        "	doctrine = doctrine_adultery_women_shunned",
        "	doctrine = doctrine_kinslaying_any_dynasty_member_crime",
        "	doctrine = doctrine_deviancy_shunned",
        "	doctrine = doctrine_witchcraft_shunned",
        "",
        "	#Clerical Functions",
        "	doctrine = doctrine_clerical_function_alms_and_pacification",
        "	doctrine = doctrine_clerical_gender_male_only",
        "	doctrine = doctrine_clerical_marriage_allowed",
        "	doctrine = doctrine_clerical_succession_temporal_appointment",
        "	",
        "	traits = {",
        "		virtues = {",
        "			",
        "		}",
        "		sins = {",
        "			",
        "		}",
        "	}",
        "",
        "	custom_faith_icons = {",
        "		 {}".format(icon_string),
        "	 }",
        "",
        "	holy_order_names = {",
        "		 ",
        "	}",
        "",
        "	holy_order_maa = { war_elephant }",
        "",
        "	localization = {",
        "		#HighGod",
        "		HighGodName = nanakpanthi_high_god_name",
        "		HighGodNamePossessive = nanakpanthi_high_god_name_possessive",
        "		HighGodNameSheHe = CHARACTER_SHEHE_THEM",
        "		HighGodHerselfHimself = CHARACTER_THEMSELF",
        "		HighGodHerHis = CHARACTER_HERHIS_THEIR",
        "		HighGodNameAlternate = nanakpanthi_high_god_name_alternate",
        "		HighGodNameAlternatePossessive = nanakpanthi_high_god_name_alternate_possessive",
        "",
        "		#Creator",
        "		CreatorName = nanakpanthi_creator_god_name",
        "		CreatorNamePossessive = nanakpanthi_creator_god_name_possessive",
        "		CreatorSheHe = CHARACTER_SHEHE_HE",
        "		CreatorHerHis = CHARACTER_HERHIS_HIS",
        "		CreatorHerHim = CHARACTER_HERHIM_HIM",
        "",
        "		#HealthGod",
        "		HealthGodName = nanakpanthi_health_god_name",
        "		HealthGodNamePossessive = nanakpanthi_health_god_name_possessive",
        "		HealthGodSheHe = CHARACTER_SHEHE_SHE",
        "		HealthGodHerHis = CHARACTER_HERHIS_HER",
        "		HealthGodHerHim = CHARACTER_HERHIM_HER",
        "		",
        "		#FertilityGod",
        "		FertilityGodName = nanakpanthi_fertility_god_name",
        "		FertilityGodNamePossessive = nanakpanthi_fertility_god_name_possessive",
        "		FertilityGodSheHe = CHARACTER_SHEHE_SHE",
        "		FertilityGodHerHis = CHARACTER_HERHIS_HER",
        "		FertilityGodHerHim = CHARACTER_HERHIM_HER",
        "",
        "		#WealthGod",
        "		WealthGodName = nanakpanthi_wealth_god_name",
        "		WealthGodNamePossessive = nanakpanthi_wealth_god_name_possessive",
        "		WealthGodSheHe = CHARACTER_SHEHE_HE",
        "		WealthGodHerHis = CHARACTER_HERHIS_HIS",
        "		WealthGodHerHim = CHARACTER_HERHIM_HIM",
        "",
        "		#HouseholdGod",
        "		HouseholdGodName = nanakpanthi_household_god_name",
        "		HouseholdGodNamePossessive = nanakpanthi_household_god_name_possessive",
        "		HouseholdGodSheHe = CHARACTER_SHEHE_SHE",
        "		HouseholdGodHerHis = CHARACTER_HERHIS_HER",
        "		HouseholdGodHerHim = CHARACTER_HERHIM_HER",
        "",
        "		#FateGod",
        "		FateGodName = nanakpanthi_fate_god_name",
        "		FateGodNamePossessive = nanakpanthi_fate_god_name_possessive",
        "		FateGodSheHe = CHARACTER_SHEHE_IT",
        "		FateGodHerHis = CHARACTER_HERHIS_ITS",
        "		FateGodHerHim = CHARACTER_HERHIM_IT",
        "",
        "		#KnowledgeGod",
        "		KnowledgeGodName = nanakpanthi_knowledge_god_name",
        "		KnowledgeGodNamePossessive = nanakpanthi_knowledge_god_name_possessive",
        "		KnowledgeGodSheHe = CHARACTER_SHEHE_SHE",
        "		KnowledgeGodHerHis = CHARACTER_HERHIS_HER",
        "		KnowledgeGodHerHim = CHARACTER_HERHIM_HER",
        "",
        "		#WarGod",
        "		WarGodName = nanakpanthi_war_god_name",
        "		WarGodNamePossessive = nanakpanthi_war_god_name_possessive",
        "		WarGodSheHe = CHARACTER_SHEHE_SHE",
        "		WarGodHerHis = CHARACTER_HERHIS_HER",
        "		WarGodHerHim = CHARACTER_HERHIM_HER",
        "",
        "		#TricksterGod",
        "		TricksterGodName = nanakpanthi_trickster_god_name",
        "		TricksterGodNamePossessive = nanakpanthi_trickster_god_name_possessive",
        "		TricksterGodSheHe = CHARACTER_SHEHE_HE",
        "		TricksterGodHerHis = CHARACTER_HERHIS_HIS",
        "		TricksterGodHerHim = CHARACTER_HERHIM_HIM",
        "",
        "		#NightGod",
        "		NightGodName = nanakpanthi_night_god_name",
        "		NightGodNamePossessive = nanakpanthi_night_god_name_possessive",
        "		NightGodSheHe = CHARACTER_SHEHE_SHE",
        "		NightGodHerHis = CHARACTER_HERHIS_HER",
        "		NightGodHerHim = CHARACTER_HERHIM_HER",
        "",
        "		#WaterGod",
        "		WaterGodName = nanakpanthi_water_god_name",
        "		WaterGodNamePossessive = nanakpanthi_water_god_name_possessive",
        "		WaterGodSheHe = CHARACTER_SHEHE_SHE",
        "		WaterGodHerHis = CHARACTER_HERHIS_HER",
        "		WaterGodHerHim = CHARACTER_HERHIM_HER",
        "",
        "",
        "		PantheonTerm = religion_the_gods",
        "		PantheonTermHasHave = pantheon_term_have",
        "		GoodGodNames = {",
        "			nanakpanthi_high_god_name",
        "			nanakpanthi_creator_god_name",
        "			nanakpanthi_health_god_name",
        "			nanakpanthi_fertility_god_name",
        "			nanakpanthi_wealth_god_name",
        "			nanakpanthi_household_god_name",
        "			nanakpanthi_fate_god_name",
        "			nanakpanthi_knowledge_god_name",
        "			nanakpanthi_war_god_name",
        "			nanakpanthi_trickster_god_name",
        "			nanakpanthi_night_god_name",
        "			nanakpanthi_water_god_name",
        "		}",
        "		DevilName = nanakpanthi_devil_name",
        "		DevilNamePossessive = nanakpanthi_devil_name_possessive",
        "		DevilSheHe = CHARACTER_SHEHE_THEY",
        "		DevilHerHis = CHARACTER_HERHIS_THEIR",
        "		DevilHerselfHimself = nanakpanthi_devil_herselfhimself",
        "		EvilGodNames = {",
        "			nanakpanthi_devil_name",
        "			nanakpanthi_death_name",
        "			nanakpanthi_witch_god_name",
        "		}",
        "		HouseOfWorship = nanakpanthi_house_of_worship",
        "		HouseOfWorshipPlural = nanakpanthi_house_of_worship_plural",
        "		ReligiousSymbol = nanakpanthi_religious_symbol",
        "		ReligiousText = nanakpanthi_religious_text",
        "		ReligiousHeadName = nanakpanthi_religious_head_title",
        "		ReligiousHeadTitleName = nanakpanthi_religious_head_title_name",
        "		DevoteeMale = nanakpanthi_devotee_male",
        "		DevoteeMalePlural = nanakpanthi_devotee_male_plural",
        "		DevoteeFemale = nanakpanthi_devotee_female",
        "		DevoteeFemalePlural = nanakpanthi_devotee_female_plural",
        "		DevoteeNeuter = nanakpanthi_devotee_neuter",
        "		DevoteeNeuterPlural = nanakpanthi_devotee_neuter_plural",
        "		PriestMale = nanakpanthi_priest",
        "		PriestMalePlural = nanakpanthi_priest_plural",
        "		PriestFemale = nanakpanthi_priest",
        "		PriestFemalePlural = nanakpanthi_priest_plural",
        "		PriestNeuter = nanakpanthi_priest",
        "		PriestNeuterPlural = nanakpanthi_priest_plural",
        "		AltPriestTermPlural = nanakpanthi_priest_term_plural",
        "		BishopMale = nanakpanthi_bishop",
        "		BishopMalePlural = nanakpanthi_bishop_plural",
        "		BishopFemale = nanakpanthi_bishop",
        "		BishopFemalePlural = nanakpanthi_bishop_plural",
        "		BishopNeuter = nanakpanthi_bishop",
        "		BishopNeuterPlural = nanakpanthi_bishop_plural",
        "		DivineRealm = nanakpanthi_divine_realm",
        "		PositiveAfterLife = nanakpanthi_positive_afterlife",
        "		NegativeAfterLife = nanakpanthi_negative_afterlife",
        "		DeathDeityName = nanakpanthi_death_name",
        "		DeathDeityNamePossessive = nanakpanthi_death_name_possessive",
        "		DeathDeitySheHe = CHARACTER_SHEHE_HE",
        "		DeathDeityHerHis = CHARACTER_HERHIS_HIS",
        "		WitchGodName = nanakpanthi_witch_god_name",
        "		WitchGodHerHis = CHARACTER_HERHIS_HER",
        "		WitchGodSheHe = CHARACTER_SHEHE_SHE",
        "		WitchGodHerHim = CHARACTER_HERHIM_HER",
        "		WitchGodMistressMaster = mistress",
        "		WitchGodMotherFather = mother",
        "",
        "		GHWName = ghw_great_holy_war",
        "		GHWNamePlural = ghw_great_holy_wars",
        "	}",
        "",
        "	faiths = {",
        "		sikhism = {",
        "			color = { 0 0 0 }",
        "			icon = sikh",
        "			",
        "			holy_site = abbotsford",
        "			holy_site = yuma",
        "			holy_site = mississauga",
        "			holy_site = calgary_sikh",
        "			holy_site = manhattan",
        "",
        "			doctrine = tenet_unrelenting_faith",
        "			doctrine = tenet_reincarnation",
        "			doctrine = tenet_option_for_the_poor",
        "		}",
        "		",
        "	}",
        "}",
        ""
    ]

    return template


def set_custom_icons(file: pathlib.Path, start: int, end: int) -> typing.List[str]:
    log.info("Scanning [{}]".format(file.name))

    lines = file.read_text(encoding="utf-8").splitlines(keepends=False)
    new_lines = []
    icon_string = " ".join(["custom{}".format(x) for x in range(start, end + 1)])

    # empty file check
    if len(lines) <= 1:
        return get_template(icon_string)
    else:
        in_custom_faith_icons = False
        for line in lines:
            if in_custom_faith_icons:
                if "}" in line:
                    in_custom_faith_icons = False
                else:
                    new_lines.append("\t\t{}".format(icon_string))
                    continue

            if "custom_faith_icons" in line:
                in_custom_faith_icons = True

            new_lines.append(line)

    return new_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("religion_path", help="Path to folder containing religions to be converted")
    parser.add_argument("start_number", type=int, help="First number for custom religion icons")
    parser.add_argument("end_number", type=int, help="Last number for custom religion icons")
    parser.add_argument("--dry_run", action="store_true", help="Does not move or delete files, just parse")
    parser.add_argument("--wipe", action="store_true", help="Does not backup original files")
    args = parser.parse_args()

    religion_folder = pathlib.Path(args.religion_path).resolve().absolute()
    log.info("Parsing religion icons in [{}]".format(religion_folder))

    backup_folder = religion_folder.parent.joinpath("{}.bak".format(religion_folder.name))
    if args.wipe:
        common.clear_backup_folder(backup_folder)
    else:
        common.backup_files(religion_folder, backup_folder, args.dry_run)

    for religion in sorted([x for x in religion_folder.iterdir() if x.is_file()]):
        new_contents = set_custom_icons(religion, args.start_number, args.end_number)
        if not args.dry_run:
            religion.write_text("\n".join(new_contents), encoding="utf-8")

    log.info("Conversion complete")
