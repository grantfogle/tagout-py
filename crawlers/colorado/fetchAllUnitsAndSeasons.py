finalArrUnit = []
finalArrSeason = []

elkCodes = ['EE001E1R', 'EE001O1A', 'EE002E1R', 'EE002O1A', 'EE003O1M', 'EE003O1R',
'EE003O4R', 'EE003P1R', 'EE003W1R', 'EE003W2R', 'EE003W3R', 'EE004O1A', 'EE004O1M',
'EE004O4R', 'EE004P1M', 'EE004W1R', 'EE004W2R', 'EE004W3R', 'EE005O4R', 'EE005W1R',
'EE005W2R', 'EE006O1M', 'EE006O1R', 'EE006O4R', 'EE006P1R', 'EE006W2R', 'EE007O1A',
'EE010E1R', 'EE010O1A', 'EE010W1R', 'EE011O1M', 'EE011P1R', 'EE011W1R', 'EE011W2R',
'EE012O1A', 'EE012O1M', 'EE012P1M', 'EE012W1R', 'EE012W2R', 'EE014O1M', 'EE015O1M',
'EE015O1R', 'EE015O4R', 'EE015P1R', 'EE015P2R', 'EE015P3R', 'EE015P4R', 'EE016O4R', 
'EE017O4R', 'EE018O1M', 'EE018O1R', 'EE018O4R', 'EE018P1R', 'EE018P4R', 'EE020O1A', 
'EE021O1M', 'EE021P1R', 'EE023W1R', 'EE025O1M', 'EE025W1R', 'EE027O1R', 'EE027O4R', 
'EE027P1R', 'EE027P4R', 'EE028O1M', 'EE028O1R', 'EE028O4R', 'EE028P1R', 'EE028P4R', 
'EE029O1A', 'EE033O1A', 'EE033O1M', 'EE033P4R', 'EE035O1R', 'EE035O4R', 'EE035P1R', 
'EE036O4R', 'EE039O1A', 'EE040O1A', 'EE040O1M', 'EE040O1R', 'EE040O2R', 'EE040O3R', 
'EE040O4R', 'EE040W1R', 'EE041P1R', 'EE041P4R', 'EE043O1R', 'EE043O4R', 'EE043P1R', 
'EE046O1A', 'EE048O1A', 'EE049O1A', 'EE050O1A', 'EE051O1A', 'EE053P1R', 'EE053P4R', 
'EE054O1A', 'EE055O1A', 'EE056O1A', 'EE057O1A', 'EE060O4R', 'EE060P1R', 'EE060P4R',
'EE061E1R', 'EE061O1A', 'EE062O4R', 'EE062P1R', 'EE062P4R', 'EE064O1R', 'EE064O4R',
 'EE064P1R', 'EE064P4R', 'EE066O1A', 'EE067O1A', 'EE069O1A', 'EE070P1A', 'EE070P1R', 
 'EE070P4R', 'EE071P1A', 'EE074P1A', 'EE075P1A', 'EE076O1A', 'EE077P1A', 'EE082O1M', 
 'EE082O1R', 'EE082O4R', 'EE083O1M', 'EE083O1R', 'EE083O2R', 'EE083O3R', 'EE083O4R', 
 'EE083W1R', 'EE084W1R', 'EE084W2R', 'EE085O1M', 'EE085O1R', 'EE085O4R', 'EE085P1R', 
 'EE085W1R', 'EE086O1M', 'EE086O1R', 'EE086O4R', 'EE086P1R', 'EE104O1A', 'EE104W1R', 
 'EE128O1M', 'EE133O1M', 'EE161O4R', 'EE171O4R', 'EE201E1R', 'EE201O1A', 'EE211W1R', 
 'EE214W1R', 'EE214W2R', 'EE231P2R', 'EE301W1R', 'EE301W2R', 'EE371O1R', 'EE371O4R', 
 'EE371P1R', 'EE371P4R', 'EE391O1A', 'EE441W1R', 'EE441W3R', 'EE461O1A', 'EE471O4R', 
 'EE481O1A', 'EE500O1A', 'EE501O1A', 'EE551O1A', 'EE561O1A', 'EE851J2R', 'EE851K2R', 
 'EE851K3R', 'EE851O1A', 'EE851W1R', 'EE851W2R', 'EE851W4R', 'EF001L1R', 'EF001O1M', 
 'EF001O1R', 'EF001O2R', 'EF001O3R', 'EF001O4R', 'EF001P5R', 'EF002L1R', 'EF002O1M', 
 'EF002O1R', 'EF002O2R', 'EF002O3R', 'EF002O4R', 'EF003E1R', 'EF003L1R', 'EF003O1M', 
 'EF003O1R', 'EF003O2R', 'EF003O4R', 'EF003P5R', 'EF003W1R', 'EF003W2R', 'EF003W3R', 
 'EF003W4R', 'EF003W5R', 'EF003W6R', 'EF004O1M', 'EF004O2R', 'EF004P1M', 'EF004W1R', 
 'EF004W2R', 'EF004W3R', 'EF004W4R', 'EF004W5R', 'EF004W6R', 'EF005O2R', 'EF005W1R', 
 'EF005W2R', 'EF005W3R', 'EF005W4R', 'EF005W5R', 'EF005W6R', 'EF006O1M', 'EF006O1R', 
 'EF006O2R', 'EF006O3R', 'EF006O4R', 'EF006P2R', 'EF006P3R', 'EF006P4R', 'EF006P5R', 
 'EF006W1R', 'EF006W2R', 'EF006W3R', 'EF006W4R', 'EF007L1R', 'EF007O1M', 'EF007O2R', 
 'EF007P5R', 'EF009L1R', 'EF009P5R', 'EF010L1R', 'EF010O1M', 'EF010O1R', 'EF010O2R', 
 'EF010O3R', 'EF010O4R', 'EF010P5R', 'EF010W1R', 'EF011L1R', 'EF011O1M', 'EF011O1R', 
 'EF011O2R', 'EF011O3R', 'EF011O4R', 'EF011P5R', 'EF011W1R', 'EF011W2R', 'EF011W3R', 
 'EF011W4R', 'EF011W6R', 'EF012O1M', 'EF012O2R', 'EF012P1M', 'EF012W1R', 'EF012W2R', 
 'EF012W3R', 'EF013L1R', 'EF014O1M', 'EF014O1R', 'EF014O2R', 'EF014P5R', 'EF015O1M', 
 'EF015O1R', 'EF015O2R', 'EF015P5R', 'EF016O3R', 'EF016O4R', 'EF016P3R', 'EF016P4R', 
 'EF017O3R', 'EF017O4R', 'EF017P3R', 'EF017P4R', 'EF018L1R', 'EF018O1M', 'EF018O1R', 
 'EF018O2R', 'EF018O3R', 'EF018O4R', 'EF018P5R', 'EF019L1R', 'EF019O2R', 'EF019P5R', 
 'EF020L1R', 'EF020L3R', 'EF020O1A', 'EF020O1M', 'EF020O2R', 'EF020O3R', 'EF020O4R', 
 'EF020P5R', 'EF021O1M', 'EF021O1R', 'EF021O2R', 'EF021O3R', 'EF021O4R', 'EF022L1R', 
 'EF022O2R', 'EF022O4R', 'EF022P5R', 'EF023P5R', 'EF023W1R', 'EF023W2R', 'EF023W3R', 
 'EF025O1M', 'EF025O1R', 'EF025O2R', 'EF025P5R', 'EF025W1R', 'EF025W2R', 'EF026L1R', 
 'EF027L1R', 'EF027O1R', 'EF027O2R', 'EF027O3R', 'EF027O4R', 'EF027P5R', 'EF028L1R', 
 'EF028O1M', 'EF028O1R', 'EF028O2R', 'EF028O3R', 'EF028O4R', 'EF028P5R', 'EF029O1M', 
 'EF029O1R', 'EF029O2R', 'EF029P5R', 'EF030L1R', 'EF031L1R', 'EF031O2R', 'EF032O2R', 
 'EF033O1M', 'EF033O2R', 'EF033P5R', 'EF034O2R', 'EF034P5R', 'EF035L1R', 'EF035O1M', 
 'EF035O1R', 'EF035O2R', 'EF035P5R', 'EF036O2R', 'EF036P5R', 'EF038L1R', 'EF038O1M', 
 'EF038O1R', 'EF038O2R', 'EF038P5R', 'EF039O1M', 'EF039O1R', 'EF039O2R', 'EF039P5R', 
 'EF040O1M', 'EF040O1R', 'EF040O2R', 'EF040O3R', 'EF040O4R', 'EF040P5R', 'EF040W1R', 
 'EF040W2R', 'EF041O1M', 'EF041O1R', 'EF041O2R', 'EF041P5R', 'EF042O2R', 'EF042O3R', 
 'EF042P5R', 'EF043O1M', 'EF043O1R', 'EF043O2R', 'EF043P5R', 'EF044O1M', 'EF044O1R', 
 'EF046O1M', 'EF046O1R', 'EF046O2R', 'EF046P5R', 'EF048O1M', 'EF048O2R', 'EF048O4R', 
 'EF049O1M', 'EF049O2R', 'EF049O3R', 'EF049O4R', 'EF049S2R', 'EF049S3R', 'EF049S4R', 
 'EF050L1R', 'EF050O1M', 'EF050O2R', 'EF050P5R', 'EF051O1M', 'EF051O1R', 'EF051O2R', 
 'EF051P5R', 'EF052O2R', 'EF052O3R', 'EF052P5R', 'EF053O1M', 'EF053O1R', 'EF053O2R', 
 'EF053O3R', 'EF053O4R', 'EF053P5R', 'EF054O1M', 'EF054O1R', 'EF054O2R', 'EF054O3R', 
 'EF054O4R', 'EF054P5R', 'EF055O1M', 'EF055O1R', 'EF055O2R', 'EF055O3R', 'EF055O4R', 
 'EF056O1M', 'EF056O2R', 'EF056O3R', 'EF056O4R', 'EF056P5R', 'EF057O1M', 'EF057O1R', 
 'EF057O2R', 'EF057O3R', 'EF057O4R', 'EF057P5R', 'EF059O1M', 'EF059O1R', 'EF059O2R', 
 'EF059P5R', 'EF060O1M', 'EF060O1R', 'EF060O2R', 'EF060O3R', 'EF060P5R', 'EF061O1M', 
 'EF061O1R', 'EF061O2R', 'EF061O3R', 'EF061O4R', 'EF061P5R', 'EF062O1M', 'EF062O1R', 
 'EF062O2R', 'EF062O3R', 'EF062P2R', 'EF063O1M', 'EF063O1R', 'EF063O2R', 'EF063O3R', 
 'EF063O4R', 'EF063P5R', 'EF064O1M', 'EF064O1R', 'EF064O2R', 'EF064O3R', 'EF064P1R', 
 'EF064P2R', 'EF064P5R', 'EF066O1M', 'EF066O1R', 'EF066O2R', 'EF066O3R', 'EF066O4R', 
 'EF067O1M', 'EF067O1R', 'EF067O2R', 'EF067O3R', 'EF067O4R', 'EF068O1M', 'EF068O2R', 
 'EF068O3R', 'EF068O4R', 'EF068P5R', 'EF069O1M', 'EF069O2R', 'EF069O3R', 'EF069O4R', 
 'EF069P5R', 'EF070O1A', 'EF070O1M', 'EF070O1R', 'EF070O2R', 'EF070O3R', 'EF070O4R', 
 'EF070P2R', 'EF070P5R', 'EF071O1A', 'EF071O1M', 'EF071O1R', 'EF071O2R', 'EF071P1R', 
 'EF071P4R', 'EF072O2R', 'EF072P5R', 'EF073O2R', 'EF073P5R', 'EF074O1A', 'EF074O1M', 
 'EF074O1R', 'EF074O2R', 'EF074P1R', 'EF074P4R', 'EF075O1A', 'EF075O1M', 'EF075O1R', 
 'EF075O2R', 'EF075P4R', 'EF076O1M', 'EF076O2R', 'EF076O3R', 'EF076O4R', 'EF077O1A', 
 'EF077O1M', 'EF077O1R', 'EF077O2R', 'EF077O3R', 'EF077O4R', 'EF077P1R', 'EF077P4R', 
 'EF077P5R', 'EF079O1M', 'EF079O1R', 'EF079O2R', 'EF079O3R', 'EF079O4R', 'EF080O1M', 
 'EF080O2R', 'EF080O3R', 'EF080O4R', 'EF080P5R', 'EF081O2R', 'EF081O3R', 'EF081O4R', 
 'EF081P5R', 'EF082O1M', 'EF082O1R', 'EF082O2R', 'EF082O3R', 'EF082O4R', 'EF083O1M', 
 'EF083O4R', 'EF083W1R', 'EF083W2R', 'EF083W3R', 'EF083W4R', 'EF083W5R', 'EF084W1R', 
 'EF084W2R', 'EF084W3R', 'EF084W5R', 'EF085L1R', 'EF085O1M', 'EF085O2R', 'EF085O3R', 
 'EF085O4R', 'EF085P5R', 'EF085P6R', 'EF085W1R', 'EF085W2R', 'EF086O1M', 'EF086O2R', 
 'EF086P5R', 'EF104O1M', 'EF104P5R', 'EF104W1R', 'EF104W2R', 'EF128L1R', 'EF131O2R', 
 'EF131P2R', 'EF131P5R', 'EF133L1R', 'EF133O1M', 'EF142L1R', 'EF161O3R', 'EF161O4R', 
 'EF161P3R', 'EF161P4R', 'EF171P3R', 'EF171P4R', 'EF181L1R', 'EF181O2R', 'EF181O3R', 
 'EF181O4R', 'EF181P5R', 'EF191L1R', 'EF191O2R', 'EF191P5R', 'EF201O1M', 'EF201O1R', 
 'EF201O2R', 'EF201O3R', 'EF201O4R', 'EF211L1R', 'EF211W1R', 'EF214O2R', 'EF214W1R', 
 'EF214W2R', 'EF214W3R', 'EF214W4R', 'EF214W5R', 'EF231O2R', 'EF301W1R', 'EF301W2R', 
 'EF301W3R', 'EF301W4R', 'EF301W5R', 'EF301W6R', 'EF301W7R', 'EF361L1R', 'EF371L1R', 
 'EF371O1R', 'EF371O2R', 'EF371O3R', 'EF371O4R', 'EF371P5R', 'EF391O1M', 'EF391P5R', 
 'EF411O2R', 'EF411O3R', 'EF411P5R', 'EF421O2R', 'EF421P5R', 'EF441W1R', 'EF441W3R', 
 'EF441W5R', 'EF441W7R', 'EF441W9R', 'EF461O1M', 'EF461O1R', 'EF461P5R', 'EF471O2R', 
 'EF471P5R', 'EF481O1M', 'EF481O2R', 'EF481P5R', 'EF500L1R', 'EF500O1M', 'EF500O2R', 
 'EF500P5R', 'EF501L1R', 'EF501O1M', 'EF501O2R', 'EF501P5R', 'EF511O1R', 'EF511O2R', 
 'EF511P5R', 'EF521O1M', 'EF521O1R', 'EF521O2R', 'EF551O1M', 'EF551O1R', 'EF551O2R', 
 'EF551O3R', 'EF551O4R', 'EF561O1M', 'EF561O2R', 'EF561O3R', 'EF561O4R', 'EF581P5R', 
 'EF591L1R', 'EF681O2R', 'EF681O3R', 'EF681O4R', 'EF682O1M', 'EF711O2R', 'EF711O4R', 
 'EF741O2R', 'EF741P5R', 'EF751P5R', 'EF851L1R', 'EF851L2R', 'EF851L3R', 'EF851O1M', 
 'EF851O3R', 'EF851W1R', 'EF851W2R', 'EF851W4R', 'EM001O1M', 'EM002O1M', 'EM007O1M', 
 'EM007O1R', 'EM007O2R', 'EM009O1R', 'EM009O2R', 'EM010O1M', 'EM011O1R', 'EM011O4R', 
 'EM012O4R', 'EM014O1R', 'EM014O4R', 'EM019O1R', 'EM019O2R', 'EM020L1R', 'EM020L2R', 
 'EM020O1A', 'EM020O1M', 'EM020O1R', 'EM020O2R', 'EM020O3R', 'EM020O4R', 'EM021O1R', 
 'EM021O4R', 'EM025O4R', 'EM026O4R', 'EM029O1M', 'EM029O1R', 'EM029O2R', 'EM033O4R', 
 'EM034O4R', 'EM035O1M', 'EM038O1M', 'EM038O1R', 'EM038O4R', 'EM039O1M', 'EM039O1R', 
 'EM039O2R', 'EM039O3R', 'EM039O4R', 'EM041O1M', 'EM041O1R', 'EM041O4R', 'EM043O1M', 
 'EM044O1A', 'EM044O1M', 'EM044O1R', 'EM044O4R', 'EM045O4R', 'EM046O1M', 'EM046O1R', 
 'EM046O2R', 'EM047O4R', 'EM048O1M', 'EM048O1R', 'EM048O2R', 'EM049O1M', 'EM049O1R', 
 'EM049O2R', 'EM050O1M', 'EM050O1R', 'EM050O2R', 'EM051O1M', 'EM051O1R', 'EM051O2R', 
 'EM053O1M', 'EM053O1R', 'EM053O4R', 'EM054O1M', 'EM054O1R', 'EM054O4R', 'EM055O1M', 
 'EM055O1R', 'EM055O4R', 'EM056O1M', 'EM056O1R', 'EM056O2R', 'EM056O3R', 'EM056O4R', 
 'EM057O1M', 'EM057O1R', 'EM057O2R', 'EM057O3R', 'EM057O4R', 'EM059O1M', 'EM059O1R', 
 'EM059O4R', 'EM060O1M', 'EM060O1R', 'EM061O1M', 'EM061O1R', 'EM061O2R', 'EM062O1M', 
 'EM062O1R', 'EM063O1M', 'EM063O1R', 'EM063O4R', 'EM064O1M', 'EM066O1M', 'EM066O1R', 
 'EM066O2R', 'EM066O3R', 'EM066O4R', 'EM067O1M', 'EM067O1R', 'EM067O2R', 'EM067O3R', 
 'EM067O4R', 'EM068O1M', 'EM068O1R', 'EM068O4R', 'EM069O1M', 'EM069O1R', 'EM069O2R', 
 'EM069O3R', 'EM069O4R', 'EM070O1A', 'EM070O1M', 'EM070O1R', 'EM070O4R', 'EM071O1A', 
 'EM071O1M', 'EM071O1R', 'EM071O4R', 'EM071P1R', 'EM071P4R', 'EM074O1A', 'EM074O1M', 
 'EM074O1R', 'EM074O4R', 'EM074P1R', 'EM074P4R', 'EM075O1A', 'EM075O1M', 'EM075O1R', 
 'EM075O4R', 'EM075P4R', 'EM076E1R', 'EM076O1M', 'EM076O1R', 'EM076O2R', 'EM076O3R', 
 'EM077O1A', 'EM077O1M', 'EM077O1R', 'EM077O4R', 'EM077P1R', 'EM077P4R', 'EM079O1M', 
 'EM079O1R', 'EM079O2R', 'EM079O3R', 'EM080O1M', 'EM080O1R', 'EM080O4R', 'EM104O1M', 
 'EM104O1R', 'EM104O2R', 'EM131O4R', 'EM133O4R', 'EM191O1R', 'EM191O2R', 'EM201O1M', 
 'EM214O1R', 'EM214O4R', 'EM231O4R', 'EM391O1M', 'EM391O1R', 'EM444O4R', 'EM461O1M', 
 'EM461O1R', 'EM481O1M', 'EM481O1R', 'EM481O2R', 'EM500O1M', 'EM500O1R', 'EM500O2R', 
 'EM501O1M', 'EM501O1R', 'EM501O2R', 'EM511O1R', 'EM511O4R', 'EM551O1M', 'EM551O1R', 
 'EM551O4R', 'EM561O1M', 'EM561O1R', 'EM561O2R', 'EM561O3R', 'EM561O4R', 'EM741O4R', 
 'EM851O1M', 'EM851O1R', 'EM851O2R', 'EM851O3R', 'EM851O4R']

for elkCode in elkCodes:
    # get unit
    unit = elkCode[2:5]
    season = elkCode[5:7]
    if unit not in finalArrUnit:
        finalArrUnit.append(unit)
    if season not in finalArrSeason:
        finalArrSeason.append(season)

finalUnitSorted = sorted(finalArrUnit)
finalSeasonSorted = sorted(finalArrSeason)

print(finalArrUnit)
print(finalSeasonSorted)