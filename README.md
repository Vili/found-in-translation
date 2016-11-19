# found-in-translation

Take job title phrases in a language with gender-neutral pronouns (i.e. equivalent to "They are a doctor"), translate them into English using Google Translate, and see what genders are attributed to the jobs (i.e. "He is a doctor").

## Results for Finnish as the source language

https://github.com/Vili/found-in-translation/blob/master/results-fi.txt

According to Google Translate, *she* is a receptionist, waitress, and model, but also astronomer, programmer, car mechanic, and IT manager. It doesn't seem that Google Translate would turn gender neutral pronouns into gender stereotypes at least in any systematic way. However, the big disparity is that Google Translate sees only 57 out of the 618 jobs as female (inclunding some translation fails), while the rest are male. The job titles in input-fi.txt are taken from https://fi.wikipedia.org/wiki/Luettelo_ammateista.

## Results for Turkish as the source language

https://github.com/Vili/found-in-translation/blob/master/results-tr.txt

According to Google Translate, *she* is an actress, librarian, secretary, stripper, etc. It seems that for tr->en Google Translate does turn gender neutral pronouns into gender stereotypes. Also, only 40 of the 729 jobs are seen as female. There seem to be many translation failures as well, though.
