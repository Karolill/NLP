import numpy as np


def bag_of_words(corpus: list) -> np.array:
    """
    An implementation of the bag og words (BoW) technique.
    :param corpus: A list of documents as strings.
    :return: An MxN array with the count of each word in tokens for each document.
    M is the number of documents and N the number of tokens used.
    """
    # Preprocessing:
    for i in range(0, len(corpus)):
        document = corpus[i].lower()
        to_change = {".": "",
                     ",": "",
                     "(": "",
                     ")": "",
                     "-": " "}
        corpus[i] = document.translate(str.maketrans(to_change))

    # Tokens, which are the words I'm interested in for articles about strike and fashion:
    tokens = ["forhandlinger", "sas", "partene", "konflikten", "sommerantrekket", "sommerkjole", "plagg"]

    # BoW:
    word_count = np.zeros((len(corpus), len(tokens)), dtype=int)

    for i, document in enumerate(corpus):
        word_list = document.split(" ")
        for j, token in enumerate(tokens):
            word_count[i, j] = word_list.count(token)

    return word_count


# For this example, a couple of articles of different topics have been chosen. The words counted in the function
# above also reflects these topics.

# From https://www.vg.no/nyheter/innenriks/i/66Lm18/sas-forhandlingene-det-beveger-seg-i-hvert-fall-i-riktig-retning
text_sas = "STOCKHOLM/OSLO (VG) Etter å sittet i forhandlinger fra lørdag morgen og natt til søndag, fortsetter partene i " \
       "SAS-konflikten forhandlingene gjennom dagen. Like før klokken 13.30 sier Skogvang til VG at de er slitne og at" \
       " det fortsatt jobbes. I 12.30-tiden går flere av partene ut til lunsj. Vi er på vei til et mål, sier Jan " \
       "Levi Skogvang leder SAS Norge flygerforening i Parat (SNF), på vei til lunsj. Det beveger seg i hvert fall " \
       "i riktig retning, at vi kommer oss gjenom problemstillingene. Og så håper jeg vi får et resultat til slutt, " \
       "sier han. NRK erfarer at løpetiden til avtalen er ett av flere punkter det forhandles om i 13-tiden. Roger " \
       "Klokset, leder i Norske SAS-flygeres forening (NSF), svarer at han ikke kan kommentere dette, eller om de har " \
       "kommet nærmere hverandre."

# From https://www.minmote.no/skjoennhet/livsstil/a/k6lpwv/min-sommerdag-victoria-nadine?utm_source=vgfront&utm_content=hovedlopet_row2_pos1&utm_medium=df-86-s2215238
text_fashion = "I spalten Min sommerdag tar vi en prat med inspirerende mennesker om deres sommerplaner, beste minner," \
               " skjønnhetsrutiner og favoritter. Denne gangen har vi tatt en prat med artisten Victoria Nadine, som " \
               "er aktuell med låten «Nakna» med «Young Royals»-stjernen Omar Rudberg. Hvordan har du det om dagen?" \
               " Jeg har det veldig fint om dagen faktisk. Skriver masse musikk og holder konserter rundt i Norge! " \
               "Endelig er det sommer igjen! Hva er ditt aller beste sommerminne? Hvordan ser det ultimate " \
               "sommerantrekket ut for deg? Det må jo være en hvilken som helst søt og behagelig sommerkjole! " \
               "Hvilket plagg henter du frem sommer etter sommer? En hvit sommerkjole som jeg kjøpte på Stradivarius " \
               "for noen år tilbake. Går aldri lei."

print(bag_of_words([text_sas, text_fashion]))
