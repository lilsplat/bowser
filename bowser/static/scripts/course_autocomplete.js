var substringMatcher = function(strs) {
  return function findMatches(q, cb) {
    var matches, substrRegex;
 
    // an array that will be populated with substring matches
    matches = [];
 
    // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, 'i');
 
    // iterate through the pool of strings and for any string that
    // contains the substring `q`, add it to the `matches` array
    $.each(strs, function(i, str) {
      if (substrRegex.test(str)) {
        // the typeahead jQuery plugin expects suggestions to a
        // JavaScript object, refer to typeahead docs for more info
        matches.push({ value: str });
      }
    });
 
    cb(matches);
  };
};
 
var states = ['AFR105', 'AFR201', 'AFR202', 'AFR206', 'AFR207', 'AFR208', 'AFR211', 'AFR212', 'AFR222', 'AFR226', 'AFR235', 'AFR238', 'AFR242', 'AFR243', 'AFR251', 'AFR252', 'AFR254', 'AFR255', 'AFR261', 'AFR265', 'AFR292', 'AFR297', 'AFR300', 'AFR301', 'AFR302', 'AFR306', 'AFR310', 'AFR316', 'AFR318', 'AFR340', 'AFR341', 'AMST101', 'AMST151', 'AMST152', 'AMST211', 'AMST212', 'AMST220', 'AMST222', 'AMST230', 'AMST240', 'AMST241', 'AMST246', 'AMST268', 'AMST274', 'AMST286', 'AMST315', 'AMST317', 'AMST318', 'AMST321', 'AMST340', 'AMST342', 'AMST344', 'AMST348', 'AMST355', 'AMST363', 'AMST364', 'ANTH104', 'ANTH107', 'ANTH110', 'ANTH201', 'ANTH204', 'ANTH206', 'ANTH207', 'ANTH209', 'ANTH209L', 'ANTH214', 'ANTH217', 'ANTH219', 'ANTH225', 'ANTH226', 'ANTH229', 'ANTH229L', 'ANTH230', 'ANTH232', 'ANTH237', 'ANTH238', 'ANTH239', 'ANTH247', 'ANTH251', 'ANTH274', 'ANTH281', 'ANTH299', 'ANTH300', 'ANTH301', 'ANTH305', 'ANTH310', 'ANTH314', 'ANTH319', 'ANTH362', 'ARAB101', 'ARAB102', 'ARAB201', 'ARAB202', 'ARAB210', 'ARAB301', 'ARAB302', 'ARAB307', 'ARTH100', 'ARTH100L', 'ARTH101', 'ARTH101L', 'ARTH150', 'ARTH175', 'ARTH200', 'ARTH201', 'ARTH202', 'ARTH203', 'ARTH205', 'ARTH218', 'ARTH221', 'ARTH224', 'ARTH225', 'ARTH226', 'ARTH228', 'ARTH230', 'ARTH231', 'ARTH232', 'ARTH236', 'ARTH238', 'ARTH240', 'ARTH241', 'ARTH242', 'ARTH244', 'ARTH245', 'ARTH246', 'ARTH247', 'ARTH248', 'ARTH251', 'ARTH255', 'ARTH256', 'ARTH259', 'ARTH262', 'ARTH263', 'ARTH266', 'ARTH289', 'ARTH290', 'ARTH292', 'ARTH299', 'ARTH302', 'ARTH303', 'ARTH309', 'ARTH311', 'ARTH312', 'ARTH316', 'ARTH318', 'ARTH319', 'ARTH320', 'ARTH329', 'ARTH331', 'ARTH333', 'ARTH334', 'ARTH335', 'ARTH336', 'ARTH338', 'ARTH340', 'ARTH341', 'ARTH344', 'ARTH345', 'ARTH346', 'ARTH369', 'ARTH373', 'ARTH380', 'ARTH388', 'ARTH391', 'ARTS105', 'ARTS106', 'ARTS108', 'ARTS109', 'ARTS113', 'ARTS165', 'ARTS207', 'ARTS208', 'ARTS210', 'ARTS216', 'ARTS217', 'ARTS218', 'ARTS219', 'ARTS220', 'ARTS221', 'ARTS222', 'ARTS255', 'ARTS260', 'ARTS265', 'ARTS303', 'ARTS307', 'ARTS308', 'ARTS313', 'ARTS314', 'ARTS315', 'ARTS317', 'ARTS321', 'ARTS322', 'ARTS362', 'ARTS365', 'ASTR100', 'ASTR100L', 'ASTR100LL', 'ASTR101', 'ASTR101L', 'ASTR101LL', 'ASTR102L', 'ASTR107', 'ASTR108', 'ASTR110', 'ASTR201', 'ASTR203', 'ASTR205', 'ASTR206', 'ASTR223', 'ASTR250GH', 'ASTR301', 'ASTR303', 'ASTR311', 'ASTR323', 'BIOC219', 'BIOC219L', 'BIOC220', 'BIOC220L', 'BIOC223', 'BIOC223L', 'BIOC240', 'BIOC320', 'BIOC320L', 'BIOC323', 'BIOC331', 'BISC104', 'BISC105', 'BISC106', 'BISC106L', 'BISC107', 'BISC108', 'BISC108L', 'BISC109', 'BISC109L', 'BISC110', 'BISC110L', 'BISC111', 'BISC111L', 'BISC111T', 'BISC112', 'BISC112L', 'BISC113', 'BISC113L', 'BISC175', 'BISC198', 'BISC201', 'BISC201L', 'BISC202', 'BISC202L', 'BISC203', 'BISC203L', 'BISC207', 'BISC207L', 'BISC209', 'BISC209L', 'BISC210', 'BISC210L', 'BISC214', 'BISC214L', 'BISC216', 'BISC216L', 'BISC219', 'BISC219L', 'BISC220', 'BISC220L', 'BISC247', 'BISC247L', 'BISC301', 'BISC302', 'BISC302L', 'BISC305', 'BISC306', 'BISC307', 'BISC307L', 'BISC308', 'BISC308L', 'BISC310', 'BISC310L', 'BISC311', 'BISC311L', 'BISC314', 'BISC314L', 'BISC315', 'BISC315L', 'BISC316', 'BISC316L', 'BISC319', 'BISC319L', 'BISC320', 'BISC320L', 'BISC321', 'BISC322', 'BISC322L', 'BISC327', 'BISC328', 'BISC331', 'BISC334', 'BISC335', 'BISC336', 'BISC338', 'BISC339', 'BISC340', 'BISC345', 'BISC345L', 'BISC347', 'BISC347L', 'BISC399', 'CAMS101', 'CAMS102', 'CAMS105', 'CAMS135', 'CAMS138', 'CAMS200', 'CAMS201', 'CAMS202', 'CAMS203', 'CAMS204', 'CAMS205', 'CAMS208', 'CAMS209', 'CAMS211', 'CAMS213', 'CAMS218', 'CAMS219', 'CAMS222', 'CAMS225', 'CAMS227', 'CAMS230', 'CAMS232', 'CAMS234', 'CAMS235', 'CAMS238', 'CAMS239', 'CAMS240', 'CAMS241', 'CAMS255', 'CAMS270', 'CAMS274', 'CAMS305', 'CAMS308', 'CAMS313', 'CAMS321', 'CAMS329', 'CAMS333', 'CAMS334', 'CAMS335', 'CAMS338', 'CAMS340', 'CAMS341', 'CAMS343', 'CAMS362', 'CAMS378', 'CHEM102', 'CHEM102L', 'CHEM105', 'CHEM105L', 'CHEM105P', 'CHEM105PL', 'CHEM106', 'CHEM107', 'CHEM120', 'CHEM120L', 'CHEM205', 'CHEM205L', 'CHEM211', 'CHEM211L', 'CHEM212', 'CHEM212L', 'CHEM220', 'CHEM221', 'CHEM221L', 'CHEM222', 'CHEM222L', 'CHEM223', 'CHEM223L', 'CHEM232', 'CHEM232L', 'CHEM233', 'CHEM233L', 'CHEM306', 'CHEM309', 'CHEM317', 'CHEM318', 'CHEM320', 'CHEM320L', 'CHEM323', 'CHEM328', 'CHEM328L', 'CHEM330', 'CHEM330L', 'CHEM331', 'CHEM334', 'CHEM335', 'CHEM335L', 'CHEM340', 'CHEM341', 'CHEM341L', 'CHEM361', 'CHEM361L', 'CHIN101', 'CHIN102', 'CHIN103', 'CHIN104', 'CHIN201', 'CHIN202', 'CHIN203', 'CHIN204', 'CHIN208', 'CHIN209', 'CHIN211', 'CHIN212', 'CHIN213', 'CHIN223', 'CHIN231', 'CHIN243', 'CHIN244', 'CHIN301', 'CHIN302', 'CHIN306', 'CHIN307', 'CHIN310', 'CHIN311', 'CHIN312', 'CHIN323', 'CHIN326', 'CHIN331', 'CHIN338', 'CHIN339', 'CHIN344', 'CLCV104', 'CLCV106', 'CLCV110', 'CLCV200', 'CLCV201', 'CLCV202', 'CLCV204', 'CLCV205', 'CLCV210', 'CLCV213', 'CLCV214', 'CLCV224', 'CLCV226', 'CLCV240', 'CLCV243', 'CLCV300', 'CLCV305', 'CLCV310', 'CLCV313', 'CLCV325', 'CLSC214', 'CLSC216', 'CLSC300', 'CPLT113', 'CPLT120', 'CPLT180', 'CPLT208', 'CPLT229', 'CPLT284', 'CPLT288', 'CPLT325', 'CPLT334', 'CS110', 'CS110L', 'CS111', 'CS111L', 'CS112', 'CS112L', 'CS114', 'CS114L', 'CS117', 'CS117L', 'CS118', 'CS118L', 'CS215', 'CS220', 'CS220L', 'CS230', 'CS230L', 'CS231', 'CS232', 'CS235', 'CS240', 'CS240L', 'CS242', 'CS249', 'CS251', 'CS304', 'CS307', 'CS310', 'CS313', 'CS315', 'CS320', 'CS322', 'CS332', 'CS332L', 'CS342', 'CS342L', 'CS349', 'EALC245', 'EALL225', 'EALL257', 'EALL325', 'EC701J', 'ECON100', 'ECON101', 'ECON102', 'ECON103', 'ECON103L', 'ECON201', 'ECON202', 'ECON203', 'ECON210', 'ECON213', 'ECON214', 'ECON220', 'ECON222', 'ECON228', 'ECON232', 'ECON236', 'ECON242', 'ECON243', 'ECON246', 'ECON302', 'ECON303', 'ECON306', 'ECON309', 'ECON310', 'ECON311', 'ECON312', 'ECON313', 'ECON314', 'ECON318', 'ECON320', 'ECON321', 'ECON322', 'ECON323', 'ECON324', 'ECON326', 'ECON331', 'ECON332', 'ECON333', 'ECON334', 'ECON335', 'ECON341', 'ECON343', 'ECON380', 'EDUC110', 'EDUC117', 'EDUC200', 'EDUC201', 'EDUC212', 'EDUC215', 'EDUC216', 'EDUC300', 'EDUC302', 'EDUC303', 'EDUC304', 'EDUC305', 'EDUC308', 'EDUC310', 'EDUC312', 'EDUC314', 'EDUC321', 'EDUC322', 'EDUC325', 'EDUC327', 'EDUC334', 'EDUC335', 'ENG103', 'ENG112', 'ENG113', 'ENG114', 'ENG115', 'ENG120', 'ENG121', 'ENG150', 'ENG202', 'ENG203', 'ENG204', 'ENG205', 'ENG206', 'ENG210', 'ENG213', 'ENG222', 'ENG223', 'ENG224', 'ENG225', 'ENG227', 'ENG234', 'ENG241', 'ENG245', 'ENG247', 'ENG249', 'ENG251', 'ENG253', 'ENG262', 'ENG266', 'ENG267', 'ENG268', 'ENG269', 'ENG271', 'ENG272', 'ENG273', 'ENG274', 'ENG277', 'ENG281', 'ENG282', 'ENG283', 'ENG285', 'ENG286', 'ENG287', 'ENG290', 'ENG301', 'ENG302', 'ENG315', 'ENG320', 'ENG324', 'ENG325', 'ENG335', 'ENG345', 'ENG349', 'ENG351', 'ENG355', 'ENG363', 'ENG364', 'ENG382', 'ENG383', 'ENG384', 'ENG385', 'ENG387', 'ENG388', 'ENG390', 'ENGR160', 'ES101', 'ES101L', 'ES102', 'ES103', 'ES111', 'ES201', 'ES201L', 'ES203', 'ES210', 'ES210L', 'ES212', 'ES214', 'ES215', 'ES216', 'ES218', 'ES220', 'ES220L', 'ES226', 'ES228', 'ES229', 'ES247', 'ES247L', 'ES289', 'ES299', 'ES300', 'ES307', 'ES307L', 'ES312', 'ES312S', 'ES313', 'ES315', 'ES315L', 'ES325', 'ES327', 'ES347', 'ES347L', 'ES381', 'ES383', 'ES399', 'EXTD105', 'EXTD106', 'EXTD110', 'EXTD111', 'EXTD120', 'EXTD123', 'EXTD124', 'EXTD125', 'EXTD128', 'EXTD160', 'EXTD220', 'EXTD220L', 'EXTD225', 'EXTD226', 'FREN101', 'FREN102', 'FREN103', 'FREN150', 'FREN151', 'FREN201', 'FREN202', 'FREN203', 'FREN205', 'FREN206', 'FREN207', 'FREN208', 'FREN209', 'FREN210', 'FREN211', 'FREN213', 'FREN214', 'FREN217', 'FREN218', 'FREN221', 'FREN222', 'FREN224', 'FREN225', 'FREN226', 'FREN228', 'FREN229', 'FREN230', 'FREN232', 'FREN233', 'FREN234', 'FREN303', 'FREN306', 'FREN308', 'FREN313', 'FREN314', 'FREN315', 'FREN319', 'FREN323', 'FREN324', 'FREN327', 'FREN331', 'FREN332', 'FREN333', 'FREN334', 'FREN335', 'FREN349', 'GEOS101', 'GEOS101L', 'GEOS102', 'GEOS102L', 'GEOS106', 'GEOS111', 'GEOS200', 'GEOS200L', 'GEOS201', 'GEOS201L', 'GEOS203', 'GEOS206', 'GEOS208', 'GEOS210', 'GEOS210L', 'GEOS213', 'GEOS216', 'GEOS218', 'GEOS218L', 'GEOS220', 'GEOS220W', 'GEOS223', 'GEOS230', 'GEOS302', 'GEOS302L', 'GEOS304', 'GEOS304L', 'GEOS306', 'GEOS313', 'GEOS315', 'GEOS315L', 'GEOS316', 'GEOS318', 'GEOS318L', 'GEOS320', 'GEOS323', 'GER101', 'GER102', 'GER130', 'GER201', 'GER202', 'GER202W', 'GER232', 'GER235', 'GER236', 'GER237', 'GER239', 'GER258', 'GER260', 'GER276', 'GER280', 'GER288', 'GER290', 'GER313', 'GER325', 'GER329', 'GER376', 'GER389', 'GRK101', 'GRK102', 'GRK201', 'GRK202', 'GRK303', 'GRK304', 'GRK305', 'GRK306', 'GRK308', 'GRK309', 'HEBR101', 'HEBR102', 'HEBR201', 'HEBR202', 'HIST115', 'HIST200', 'HIST201', 'HIST203', 'HIST204', 'HIST205', 'HIST206', 'HIST207', 'HIST208', 'HIST209', 'HIST211', 'HIST212', 'HIST213', 'HIST214', 'HIST215', 'HIST220', 'HIST222', 'HIST224', 'HIST228', 'HIST229', 'HIST231', 'HIST232', 'HIST233', 'HIST234', 'HIST235', 'HIST240', 'HIST242', 'HIST243', 'HIST244', 'HIST245', 'HIST246', 'HIST247', 'HIST248', 'HIST249', 'HIST252', 'HIST253', 'HIST256', 'HIST260', 'HIST262', 'HIST263', 'HIST265', 'HIST267', 'HIST269', 'HIST270', 'HIST272', 'HIST274', 'HIST275', 'HIST276', 'HIST277', 'HIST278', 'HIST279', 'HIST280', 'HIST283', 'HIST284', 'HIST290', 'HIST293', 'HIST298', 'HIST299', 'HIST302', 'HIST307', 'HIST312', 'HIST313', 'HIST314', 'HIST319', 'HIST320', 'HIST329', 'HIST330', 'HIST334', 'HIST340', 'HIST341', 'HIST346', 'HIST347', 'HIST352', 'HIST353', 'HIST358', 'HIST359', 'HIST372', 'HIST375', 'HIST377', 'HIST379', 'HIST382', 'HIST383', 'HIST395', 'HIST396', 'HNUR101', 'HNUR102', 'HNUR201', 'HNUR201L', 'HNUR202', 'HUM380', 'ITAS101', 'ITAS102', 'ITAS103', 'ITAS104', 'ITAS201', 'ITAS202', 'ITAS202W', 'ITAS203', 'ITAS225', 'ITAS263', 'ITAS270', 'ITAS271', 'ITAS273', 'ITAS274', 'ITAS275', 'ITAS309', 'ITAS310', 'ITAS315', 'ITAS316', 'ITAS320', 'ITAS349', 'JPN101', 'JPN102', 'JPN130', 'JPN131', 'JPN201', 'JPN202', 'JPN231', 'JPN232', 'JPN251', 'JPN252', 'JPN256', 'JPN257', 'JPN308', 'JPN311', 'JPN312', 'JPN314', 'JPN315', 'JPN351', 'JPN352', 'JPN353', 'JPN355', 'JWST111', 'KOR101', 'KOR102', 'KOR201', 'KOR202', 'KOR206', 'KOR231', 'KOR232', 'KOR256', 'KOR309', 'KOR356', 'LAT101', 'LAT102', 'LAT200', 'LAT201', 'LAT301', 'LAT302', 'LAT307', 'LAT310', 'LAT315', 'LAT317', 'LING114', 'LING238', 'LING240', 'LING244', 'LING248', 'LING312', 'LING315', 'LING319', 'MATH101', 'MATH101Z', 'MATH115', 'MATH116', 'MATH120', 'MATH125', 'MATH201', 'MATH205', 'MATH206', 'MATH210', 'MATH214', 'MATH215', 'MATH220', 'MATH223', 'MATH225', 'MATH249', 'MATH302', 'MATH303', 'MATH305', 'MATH306', 'MATH307', 'MATH309', 'MATH310', 'MATH312', 'MATH322', 'MATH325', 'MATH326', 'MATH349', 'ME/R222', 'ME/R247', 'ME/R249', 'ME/R275', 'ME/R325', 'MES310', 'MES331', 'MUS101', 'MUS102H', 'MUS111', 'MUS111X', 'MUS122', 'MUS200', 'MUS201', 'MUS202', 'MUS209', 'MUS220', 'MUS222', 'MUS224', 'MUS225', 'MUS230', 'MUS235', 'MUS240', 'MUS244', 'MUS245', 'MUS275', 'MUS276', 'MUS277', 'MUS287', 'MUS300', 'MUS300A', 'MUS300B', 'MUS300C', 'MUS300D', 'MUS301', 'MUS308', 'MUS315', 'MUS322', 'MUS325', 'MUS335', 'MUS344', 'MUS345', 'MUS377', 'MUS378', 'NEUR100', 'NEUR100L', 'NEUR120', 'NEUR200', 'NEUR200L', 'NEUR250G', 'NEUR300', 'NEUR305', 'NEUR305L', 'NEUR306', 'NEUR315', 'NEUR315L', 'NEUR320', 'NEUR320L', 'NEUR325', 'NEUR325L', 'NEUR332', 'NEUR335', 'NEUR335L', 'NEUR350G', 'PEAC104', 'PEAC119', 'PEAC204', 'PEAC259', 'PEAC304', 'PEAC324', 'PEAC388', 'PHIL103', 'PHIL106', 'PHIL108', 'PHIL109', 'PHIL110', 'PHIL201', 'PHIL202', 'PHIL203', 'PHIL204', 'PHIL206', 'PHIL207', 'PHIL211', 'PHIL213', 'PHIL215', 'PHIL216', 'PHIL218', 'PHIL221', 'PHIL224', 'PHIL230', 'PHIL233', 'PHIL236', 'PHIL242', 'PHIL243', 'PHIL245', 'PHIL246', 'PHIL249', 'PHIL250', 'PHIL253', 'PHIL256', 'PHIL300', 'PHIL310', 'PHIL317', 'PHIL325', 'PHIL326', 'PHIL333', 'PHIL340', 'PHIL342', 'PHIL345', 'PHYS100', 'PHYS101', 'PHYS102', 'PHYS104', 'PHYS104L', 'PHYS106', 'PHYS106L', 'PHYS107', 'PHYS107L', 'PHYS108', 'PHYS108L', 'PHYS110', 'PHYS118', 'PHYS202', 'PHYS202L', 'PHYS207', 'PHYS210', 'PHYS216', 'PHYS222', 'PHYS302', 'PHYS305', 'PHYS306', 'PHYS310', 'PHYS311', 'PHYS314', 'PHYS320', 'POL103', 'POL109', 'POL110', 'POL111', 'POL112', 'POL114', 'POL115', 'POL1200', 'POL1210', 'POL1215', 'POL1220', 'POL1235', 'POL1247', 'POL1300', 'POL1303', 'POL1313', 'POL1316', 'POL1317', 'POL1317S', 'POL1319', 'POL1319S', 'POL1324', 'POL1324S', 'POL1331', 'POL1331S', 'POL1337', 'POL1341S', 'POL1359', 'POL1362', 'POL1381', 'POL199', 'POL2202', 'POL2204', 'POL2205', 'POL2206', 'POL2207', 'POL2208', 'POL2211', 'POL2214', 'POL2217', 'POL2219', 'POL2238', 'POL230', 'POL2301', 'POL2301S', 'POL2304', 'POL2306', 'POL2306S', 'POL2307', 'POL2307S', 'POL2308', 'POL2309S', 'POL2310', 'POL2310S', 'POL2312', 'POL2312S', 'POL2336', 'POL2353', 'POL2358', 'POL2358S', 'POL2383', 'POL299', 'POL3121', 'POL3221', 'POL3222', 'POL3223', 'POL3224', 'POL3227', 'POL3229', 'POL3239', 'POL3321', 'POL3322', 'POL3322S', 'POL3323', 'POL3325', 'POL3332S', 'POL3348', 'POL3348S', 'POL3351', 'POL3352', 'POL3352S', 'POL3354', 'POL3354S', 'POL3374', 'POL3378S', 'POL3379', 'POL4201', 'POL4240', 'POL4241', 'POL4242', 'POL4248', 'POL4249', 'POL4340', 'POL4342S', 'POL4343', 'POL4343S', 'POL4344', 'POL4344S', 'POL4345', 'POL4345S', 'POL4346', 'POL4357', 'PORT103', 'PORT203', 'PSYC101', 'PSYC205', 'PSYC205L', 'PSYC207', 'PSYC208', 'PSYC210', 'PSYC212', 'PSYC213', 'PSYC214', 'PSYC215', 'PSYC216', 'PSYC217', 'PSYC218', 'PSYC219', 'PSYC221', 'PSYC222', 'PSYC245', 'PSYC248', 'PSYC300', 'PSYC301', 'PSYC304R', 'PSYC305', 'PSYC306R', 'PSYC307R', 'PSYC308', 'PSYC310R', 'PSYC312R', 'PSYC313R', 'PSYC314R', 'PSYC316', 'PSYC318', 'PSYC319', 'PSYC321', 'PSYC321L', 'PSYC322', 'PSYC326', 'PSYC327', 'PSYC328', 'PSYC329', 'PSYC330', 'PSYC332', 'PSYC333', 'PSYC334', 'PSYC337', 'PSYC338', 'PSYC339', 'PSYC340', 'PSYC343', 'PSYC344', 'PSYC345', 'PSYC349', 'QR140', 'QR170', 'QR180', 'QR309', 'RAST212', 'RAST222', 'RAST322', 'REL100', 'REL104', 'REL105', 'REL108', 'REL109', 'REL114', 'REL115', 'REL118', 'REL119', 'REL204', 'REL205', 'REL206', 'REL208', 'REL209', 'REL211', 'REL215', 'REL216', 'REL218', 'REL220', 'REL224', 'REL225', 'REL226', 'REL230', 'REL232', 'REL240', 'REL243', 'REL244', 'REL245', 'REL247', 'REL251', 'REL252', 'REL253', 'REL254', 'REL255', 'REL257', 'REL259', 'REL260', 'REL261', 'REL262', 'REL263', 'REL267', 'REL281', 'REL290', 'REL298', 'REL301', 'REL304', 'REL307', 'REL310', 'REL319', 'REL323', 'REL326', 'REL330', 'REL342', 'REL343', 'REL357', 'REL364', 'REL368', 'REL380', 'RUSS101', 'RUSS102', 'RUSS201', 'RUSS202', 'RUSS203W', 'RUSS251', 'RUSS257', 'RUSS260', 'RUSS272', 'RUSS276', 'RUSS277', 'RUSS286', 'RUSS301', 'RUSS302', 'RUSS303W', 'RUSS333', 'RUSS334', 'RUSS343', 'RUSS376', 'RUSS386', 'SAS206', 'SAS211', 'SAS251', 'SAS252', 'SAS301', 'SAS302', 'SAS304', 'SAS331', 'SOC102', 'SOC105', 'SOC108', 'SOC114', 'SOC137', 'SOC138', 'SOC150', 'SOC190', 'SOC190L', 'SOC200', 'SOC201', 'SOC202', 'SOC204', 'SOC205', 'SOC209', 'SOC212', 'SOC217', 'SOC221', 'SOC231', 'SOC233', 'SOC234', 'SOC241', 'SOC246', 'SOC251', 'SOC289', 'SOC290', 'SOC302', 'SOC304', 'SOC306', 'SOC307', 'SOC308', 'SOC309', 'SOC310', 'SOC311', 'SOC314', 'SOC318', 'SOC319', 'SOC320', 'SOC334', 'SOC344', 'SOC348', 'SP7UR', 'SPAN101', 'SPAN102', 'SPAN110', 'SPAN201', 'SPAN202', 'SPAN241', 'SPAN242', 'SPAN245', 'SPAN252', 'SPAN253', 'SPAN254', 'SPAN257', 'SPAN258', 'SPAN259', 'SPAN260', 'SPAN261', 'SPAN262', 'SPAN263', 'SPAN264', 'SPAN265', 'SPAN266', 'SPAN267', 'SPAN268', 'SPAN269', 'SPAN271', 'SPAN272', 'SPAN273', 'SPAN274', 'SPAN275', 'SPAN277', 'SPAN279', 'SPAN300', 'SPAN302', 'SPAN305', 'SPAN307', 'SPAN314', 'SPAN315', 'SPAN318', 'SPAN320', 'SPAN323', 'SPAN324', 'SPAN325', 'SPAN327', 'SPAN329', 'SPAN335', 'SPAN337', 'SPAN340', 'SUST201', 'SUST301', 'SWA101', 'SWA102', 'SWA201', 'SWA202', 'SWA203', 'THST101', 'THST106', 'THST130', 'THST131', 'THST203', 'THST204', 'THST205', 'THST206', 'THST207', 'THST208', 'THST209', 'THST210', 'THST212', 'THST214', 'THST215', 'THST221', 'THST222', 'THST251', 'THST305', 'THST312', 'THST314', 'THST315', 'THST321', 'THST351', 'THST353', 'THST355', 'WGST100', 'WGST108', 'WGST120', 'WGST121', 'WGST150', 'WGST200', 'WGST205', 'WGST206', 'WGST207', 'WGST211', 'WGST212', 'WGST214', 'WGST216', 'WGST217', 'WGST218', 'WGST219', 'WGST220', 'WGST222', 'WGST223', 'WGST225', 'WGST235', 'WGST240', 'WGST249', 'WGST274', 'WGST299', 'WGST304', 'WGST305', 'WGST306', 'WGST310', 'WGST311', 'WGST312', 'WGST314', 'WGST317', 'WGST321', 'WGST324', 'WGST326', 'WGST340', 'WRIT105', 'WRIT106', 'WRIT107', 'WRIT108', 'WRIT109', 'WRIT110', 'WRIT111', 'WRIT112', 'WRIT113', 'WRIT114', 'WRIT115', 'WRIT120', 'WRIT121', 'WRIT122', 'WRIT123', 'WRIT124', 'WRIT125', 'WRIT125P', 'WRIT125PL', 'WRIT126', 'WRIT126H', 'WRIT130', 'WRIT131', 'WRIT132', 'WRIT133', 'WRIT134', 'WRIT135', 'WRIT136', 'WRIT137', 'WRIT138', 'WRIT139', 'WRIT140', 'WRIT141', 'WRIT142', 'WRIT143', 'WRIT144', 'WRIT145', 'WRIT146', 'WRIT147', 'WRIT149', 'WRIT150', 'WRIT159', 'WRIT160', 'WRIT161', 'WRIT162', 'WRIT163', 'WRIT164', 'WRIT165', 'WRIT166', 'WRIT167', 'WRIT168', 'WRIT169', 'WRIT170', 'WRIT171', 'WRIT172', 'WRIT199', 'WRIT199H', 'WRIT225', 'WRIT290', 'WRIT291', 'WRIT307', 'WRIT390'];
 
$('#find_course .typeahead').typeahead({
  hint: true,
  highlight: true,
  minLength: 1
},
{
  name: 'states',
  displayKey: 'value',
  source: substringMatcher(states)
});