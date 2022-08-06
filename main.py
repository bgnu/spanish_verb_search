import sqlite3

from blessed import Terminal

term = Terminal()


def connect_to_database():
    con = sqlite3.connect("spanish_verbs.db")
    return con.cursor()


def display_conjugation(verb):
    """This function accepts an infinitive and returns a cursor object with its conjugated
    forms. No compound tenses are returned, nor are the past or present participles."""
    sql = (
        f"SELECT tense, verb_english, form_1s, form_2s, form_3s, form_1p, form_2p, form_3p "
        f"FROM verbs "
        f"WHERE infinitive='{verb}' "
        f"AND mood='Indicativo' "
        f"AND NOT tense='Condicional perfecto' "
        f"AND NOT tense='Futuro perfecto' "
        f"AND NOT tense='Pluscuamperfecto' "
        f"AND NOT tense='Presente perfecto' "
        f"AND NOT tense='Pretérito anterior' "
    )

    cursor_obj.execute(sql)
    rows = cursor_obj.fetchall()
    # annoyingly this is where incorrect sql queries are spotted.
    if len(rows) == 0:
        print("Verb not found")
        return None

    ljustified_rows = []
    for lst in rows:
        ljustified_rows.append([conjugate.ljust(24, " ") for conjugate in lst])
    top_line = f"\n{term.gold}\t\t\t{term.gold_underline}Present{term.normal}\t\t\t{term.gold_underline}Preterite{term.normal}\t\t{term.gold_underline}Imperfect{term.normal}\t\t{term.gold_underline}Conditional{term.normal}\t\t{term.gold_underline}Future{term.normal}\n"

    print(top_line)
    # First person singular
    print(
        f"{term.lawngreen}yo{term.normal}\t\t\t{term.lawngreen}{ljustified_rows[3][2]}"
        f"{ljustified_rows[4][2]}"
        f"{ljustified_rows[2][2]}"
        f"{ljustified_rows[0][2]}"
        f"{ljustified_rows[1][2]}{term.normal}"
    )  # should be present, preterite, imperfect, conditional, future

    # Second person singular
    print(
        f"{term.khaki1}tú{term.normal}\t\t\t{term.khaki1}{ljustified_rows[3][3]}"
        f"{ljustified_rows[4][3]}"
        f"{ljustified_rows[2][3]}"
        f"{ljustified_rows[0][3]}"
        f"{ljustified_rows[1][3]}{term.normal}"
    )  # should be present, preterite, imperfect, conditional, future

    # Third person singular
    print(
        f"{term.palegoldenrod}él/ella/Ud.{term.normal}\t\t{term.palegoldenrod}{ljustified_rows[3][4]}"
        f"{ljustified_rows[4][4]}"
        f"{ljustified_rows[2][4]}"
        f"{ljustified_rows[0][4]}"
        f"{ljustified_rows[1][4]}{term.normal}"
    )  # should be present, preterite, imperfect, conditional, future

    # First person plural
    print(
        f"{term.olivedrab2}nosotros{term.normal}\t\t{term.olivedrab2}{ljustified_rows[3][5]}"
        f"{ljustified_rows[4][5]}"
        f"{ljustified_rows[2][5]}"
        f"{ljustified_rows[0][5]}"
        f"{ljustified_rows[1][5]}{term.normal}"
    )  # should be present, preterite, imperfect, conditional, future

    # Second person plural
    print(
        f"{term.aquamarine2}vosotros{term.normal}\t\t{term.aquamarine2}{ljustified_rows[3][6]}"
        f"{ljustified_rows[4][6]}"
        f"{ljustified_rows[2][6]}"
        f"{ljustified_rows[0][6]}"
        f"{ljustified_rows[1][6]}{term.normal}"
    )  # should be present, preterite, imperfect, conditional, future

    # Third person plural
    print(
        f"{term.slategray1}ellos/ellas/Uds.{term.normal}\t{term.slategray1}{ljustified_rows[3][7]}"
        f"{ljustified_rows[4][7]}"
        f"{ljustified_rows[2][7]}"
        f"{ljustified_rows[0][7]}"
        f"{ljustified_rows[1][7]}{term.normal}"
    )  # should be present, preterite, imperfect, conditional, future


if __name__ == "__main__":
    cursor_obj = connect_to_database()
    while True:
        verb = input(f"Please enter a verb: ")
        if verb == "end":
            print("Thanks, goodbye!")
            break
        display_conjugation(verb)
