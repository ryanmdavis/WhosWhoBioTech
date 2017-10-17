from WhosWho import WhosWhoBioTech

wwbt=WhosWhoBioTech()

print '\n\n******************************************************\nExample 1: liquid biopsy'
whos_who=wwbt.ww('liquid biopsy')
print '\nExplanation for liquid biopsy query results:\n'
print 'Michael Stocum: CEO of Inivata, which just entered liquid biopsy collaboration with Genomics England'
print 'Illumina: Most prominant maker of genome sequencing tools for liquid biopsy'
 
print '\n\n******************************************************\nExample 2: antibiotic'
whos_who=wwbt.ww('antibiotic')
print '\nExplanation for antibiotic query results:\n'
print 'FDA: The Food and Drug Administration.  FDA must approve all new antibiotics before human use'
print 'Motif Bio & Iclaprim:  Motif Biosciences\' new drug Iclaprim is a new antibiotic designed to be effective against resistant bacteria'
print 'AMRC: Centre for Antimicrobial Resistance: a joint private-public initiative to support/accelerate the development of new antibiotics and diagnostics'
print 'MBLI: Technically not a person or organization.  MBLI is a drug against antibiotic-resistant bacteria.'
print 'Warp Drive CEO Laurence Reid: Warp Drive\' aminoglycoside antibiotic program was just bought by Sanofi for $750M.  Warp Drive\' CEO is Laurence Reid'

print '\n\n******************************************************\nExample 3: immunotherapy'
whos_who=wwbt.ww('immunotherapy')
print '\nExplanation for immunotherapyd query results:\n'
print 'Immatics & ACTolog: Immatics is a biotech company that makes ACTolog, a product which pulls out cells from patients blood for processing.'
print 'Cancer Moonshot: NIH program to fund new cancer diagnostics and therapies'
print 'Wellington Partners and Hopp Biotech Holding: Big investors in cancer immunotherapy'