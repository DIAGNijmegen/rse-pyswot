# DO NOT EDIT THIS FILE, CHANGES WILL BE OVERWRITTEN BY update_vendor.py
# From https://github.com/JetBrains/swot.git@8ed1cc7b

STOPLIST = frozenset(
    [
        "2020.gsm.cocite.pt",
        "365.cleu.edu.mx",
        "365.mokwon.ac.kr",
        "365.ntcu.edu.tw",
        "90888.cc",
        "aaedu.edu.pl",
        "aaup.edu",
        "abcda.tech",
        "abie.ac.in",
        "ac.eap.gr",
        "academico.ifg.edu.br",
        "academico.ifmg.edu.br",
        "acarballeira.es",
        "ad1.nutc.edu.tw",
        "aejuliodinis.edu.pt",
        "ahlg.ac.cn",
        "ahzyygz.edu.cn",
        "aim.edu",
        "aims.edu",
        "aiub.edu",
        "al.insper.edu.br",
        "alex2.moe.edu.eg",
        "alexu.edu.eg",
        "allianceinternationalschool.com",
        "alpha.edu.pk",
        "alu.comillas.edu",
        "alu.hdu.edu.cn",
        "alu.hdu.edu.cn",
        "alu.uap.edu.pe",
        "alum.ccu.edu.tw",
        "alum.mit.edu",
        "alum.ubc.ca",
        "alum.urmc.rochester.edu",
        "alum.urmc.rochester.edu",
        "alum.us.es",
        "alumni.albany.edu",
        "alumni.anu.edu.au",
        "alumni.bham.ac.uk",
        "alumni.cmu.edu",
        "alumni.edu.vn",
        "alumni.habib.edu.pk",
        "alumni.hust.edu.cn",
        "alumni.imperial.ac.uk",
        "alumni.iu.edu",
        "alumni.manchester.ac.uk",
        "alumni.montclair.edu",
        "alumni.msoe.edu",
        "alumni.nottingham.ac.uk",
        "alumni.npust.edu.tw",
        "alumni.pku.edu.cn",
        "alumni.sjtu.edu.cn",
        "alumni.ssst.edu.ba",
        "alumni.stanford.edu",
        "alumni.stu.edu.cn",
        "alumni.tku.edu.tw",
        "alumni.ubc.ca",
        "alumni.ubc.ca",
        "alumni.unc.edu",
        "alumni.usp.br",
        "alumni.vcu.edu",
        "alumni.zstu.edu.cn",
        "alumno.buap.mx",
        "alumno.uaemex.mx",
        "alumno.udg.mx",
        "alumno.uned.es",
        "alumnos.uady.mx",
        "alumnos.uai.edu.ar",
        "alumnos.uninorte.edu.py",
        "alumnos.unp.edu.pe",
        "alumnos.uteg.edu.mx",
        "alumnos.utn.edu.mx",
        "aluno.ies.edu.br",
        "aluno.unb.br",
        "aluno.uniasselvi.com.br",
        "aluno.unicarioca.edu.br",
        "aluno.unip.br",
        "alunos.colegiosaogoncalo.pt",
        "alunos.estacio.br",
        "alunos.isel.pt",
        "alunos.unisagrado.edu.br",
        "alunosatc.edu.br",
        "america.edu",
        "amity.edu",
        "amu.edu.et",
        "anadolu.edu.tr",
        "anhembimorumbi.edu.br",
        "app",
        "apus.edu",
        "archten.croydon.sch.uk",
        "art.dmu.edu.eg",
        "art.edu.lv",
        "asoiu.edu.az",
        "asu.edu",
        "asu.edu.eg",
        "ataa.sch.sa",
        "aths.ac.ae",
        "atsu.edu.ge",
        "au.edu",
        "aub.edu",
        "aufe.edu.cn",
        "aurora.ekof.bg.ac.rs",
        "ausbildungswolken.de",
        "aust.edu.lb",
        "australia.edu",
        "aya.yale.edu",
        "ayit.edu.cn",
        "ayit.edu.cn",
        "az-npu.org",
        "azhar.edu.eg",
        "azhar.edu.eg",
        "azwestern.edu",
        "bahcesehir.edu.tr",
        "barstow.edu",
        "bartoncougars.org",
        "batce.edu.tt",
        "batestech.edu",
        "baypath.edu",
        "bbc.edu.cn",
        "bcmail.cuny.edu",
        "behera1.moe.edu.eg",
        "bese.ac.cn",
        "bestlistbase.com",
        "bfsu.edu.cn",
        "bgu.edu.kg",
        "binus.ac.id",
        "bit.edu.cn",
        "bitzh.edu.cn",
        "bjdx.ac.cn",
        "bjlg.ac.cn",
        "bjtu.edu.cn",
        "bnu.edu.cn",
        "boscuos.com",
        "boun.edu.tr",
        "bsu.edu.az",
        "bsu.edu.eg",
        "bub.edu.bh",
        "bub.edu.bh",
        "buc.blinn.edu",
        "buc.edu.eg",
        "bucea.edu.cn",
        "buet.ac.bd",
        "bupt.cn",
        "caa.columbia.edu",
        "caa.edu.cn",
        "cacc.edu",
        "caccmail.cacc.edu",
        "calamba.sti.edu.ph",
        "caledonian.ac.uk",
        "californiacolleges.edu",
        "campoalegre.edu.gt",
        "campus.mccd.edu",
        "campusucc.edu.co",
        "campusvirtual.aunarvillavicencio.edu.co",
        "case.edu",
        "cau.edu.cn",
        "cb.students.amrita.edu",
        "cba.edu.kw",
        "cc.ntut.edu.tw",
        "cc.peralta.edu",
        "ccc.edu",
        "cccd.edu",
        "cccs.edu",
        "ccnu.edu.cn",
        "ccsf.edu",
        "ccu.edu.tw",
        "cczu.edu.cn",
        "cdmc.edu.cn",
        "ced.alliance.edu.in",
        "cet.edu",
        "ceuandalucia.es",
        "cf",
        "chasefreedomactivate.com",
        "chc.edu.tw",
        "chd.edu.cn",
        "cheoa.studio",
        "ci.suez.edu.eg",
        "cibertec.edu.pe",
        "cic.pt",
        "cientifica.edu.pe",
        "cihanuniversity.org",
        "cis.edu.eg",
        "cit.edu",
        "cit.just.edu.jo",
        "cjlu.edu.cn",
        "clackamas.edu",
        "clatsopcc.edu",
        "cloudlearn.tech",
        "cmru.ac.th",
        "cochise.edu",
        "cocite.pt",
        "codesra.cn",
        "coep.ac.in",
        "colc.co",
        "colegio-venecia.edu.mx",
        "colegio.univalle.edu",
        "colegiotorremalmuerta.es",
        "collegelacite.ca",
        "collin.edu",
        "collin.edu",
        "conalep.edu.mx",
        "conestogac.on.ca",
        "connect.hku.hk",
        "continental.edu.pe",
        "continental.edu.pe",
        "converse.edu",
        "correo.icesi.edu.co",
        "correo.itm.edu.co",
        "correo.uis.edu.co",
        "correo.usbcali.edu.co",
        "correoaiep.cl",
        "cougarmail.collin.edu",
        "cpcc.edu",
        "cpru.ac.th",
        "cqu.edu.cn",
        "cque.edu.cn",
        "crru.ac.th",
        "csiriicb.in",
        "csn.edu.pk",
        "csu.ph",
        "cta.edu.vn",
        "ctgu.edu.cn",
        "cu.edu.kg",
        "cug.edu.cn",
        "cuiatd.edu.pk",
        "cumt.edu.cn",
        "cumtb.edu.cn",
        "cuu.ac.ug",
        "cwru.edu",
        "daihocyhanoi.edu.vn",
        "dakahliya1.moe.edu.eg",
        "dankook.ac.kr",
        "dartmouth.edu",
        "dartmouth.edu",
        "davidsonccc.edu",
        "dcic.me",
        "deltacollege.edu",
        "dhu.edu.cn",
        "dillard.edu",
        "diogocao.edu.pt",
        "dlsud.edu.ph",
        "dlut.edu.cn",
        "dnmd.fun",
        "dome.tu.ac.th",
        "dpu.ac.th",
        "dragons.hutchcc.edu",
        "dtcc.edu",
        "dxss.ac.cn",
        "dyptc.edu.in",
        "dzxy.ntu.edu.cn",
        "e.gzhu.edu.cn",
        "e.tlu.edu.vn",
        "eafit.edu.co",
        "eaglesvale.ac.zw",
        "eap.gr",
        "eastafricauniversity.net",
        "ecu.edu.eg",
        "ecupl.edu.cn",
        "ecust.edu.cn",
        "ecut.edu.cn",
        "edu.azores.gov.pt",
        "edu.cdsj6.edu.mo",
        "edu.em-lyon.com",
        "edu.hmu.gr",
        "edu.icoremail.net",
        "edu.moi",
        "edu.sorbonne-paris-nord.fr",
        "edu.tanta.edu.eg",
        "edu.uca.ma",
        "edu.umi.ac.ma",
        "edu.univali.br",
        "educn.ac.cn",
        "elcamino.edu",
        "elcamino.edu",
        "email",
        "email.axc.edu.gr",
        "email.phoenix.edu",
        "email.psu.ac.th",
        "email.tjc.edu",
        "email.zzuli.edu.cn",
        "emlmuak.cn",
        "enayu.com",
        "esoft.academy",
        "esore.asia",
        "espoch.edu.ec",
        "espol.edu.ec",
        "esprims.tn",
        "est.emi.edu.bo",
        "est.umet.edu.ec",
        "est.unev.edu.do",
        "est.ups.edu.ec",
        "estudiantes.cordillera.edu.ec",
        "estudiantes.edu.ec",
        "estudiantesunap.cl",
        "etudiant.edcparis.edu",
        "eufe.edu.ht",
        "eurasia.edu",
        "everettcc.edu",
        "faculdadefia.edu.br",
        "fagr.bu.edu.eg",
        "fairhillshs.vic.edu.au",
        "fatecie.edu.br",
        "fet.ju.edu.jo",
        "feucanvas.edu.ph",
        "fh-htachur.ch",
        "fh-schwaebischhall.de",
        "fh.unair.ac.id",
        "fhss.sjp.ac.lk",
        "fhss.sjp.ac.lk",
        "fjys.edu.cn",
        "fnur.bu.edu.eg",
        "fountaingatesc.vic.edu.au",
        "fpt.edu.vn",
        "freenet.kg",
        "freenet.kg",
        "fudan.edu.cn",
        "fue.edu.eg",
        "futa.edu.ng",
        "fvcc.edu",
        "fwu.edu.np",
        "ga",
        "gagpk.ru",
        "gduf.edu.cn",
        "geu.ac.in",
        "ghanacu.org",
        "ghazanthemprep.org",
        "giant.cos.edu",
        "giki.edu.pk",
        "go.edu.tw",
        "go.minnstate.edu",
        "go.pasadena.edu",
        "go.shoreline.edu",
        "gq",
        "graduate.hku.hk",
        "gsm.cocite.pt",
        "gtc.edu",
        "gtu.edu.tr",
        "gulfuniversity.edu.bh",
        "gydx.ac.cn",
        "gzhtcm.edu.cn",
        "gzhu.edu.cn",
        "hainanu.edu.cn",
        "hainu.edu.cn",
        "hait.edu.cn",
        "hait.edu.cn",
        "harran.edu.tr",
        "haust.edu.cn",
        "hawkmail.hccfl.edu",
        "haywood.edu",
        "hbdx.ac.cn",
        "hbtcm.edu.cn",
        "hbu.edu.cn",
        "hbut.edu.cn",
        "hc.edu.tw",
        "hcc.edu.tw",
        "hcmup.edu.vn",
        "helwan.edu.eg",
        "henu.edu.cn",
        "hhu.edu.cn",
        "hiast.edu.vn",
        "hndx.ac.cn",
        "hnit.ed.cn",
        "hnu.edu.cn",
        "hnulinton.org",
        "holmescc.edu",
        "howardcc.edu",
        "hqu.edu.cn",
        "hrbeu.edu.cn",
        "hs-darmstadt.de",
        "hsc.pku.edu.cn",
        "hstu.info",
        "htl-steyr.ac.at",
        "huaf.edu.vn",
        "huanghuai.edu.cn",
        "hubu.edu.cn",
        "hufe.edu.cn",
        "hufi.edu.vn",
        "hunnu.edu.cn",
        "huse.edu.cn",
        "hust.edu.cn",
        "hust.edu.kg",
        "hust.edu.vn",
        "hznu.edu.cn",
        "ibero.edu.co",
        "ibero.edu.co",
        "icamtech.com",
        "icc.edu",
        "icu-edu.org",
        "idat.edu.pe",
        "iga-marrakech.ma",
        "imghost.tech",
        "imnu.edu.cn",
        "imt.ac.in",
        "inacapmail.cl",
        "indoamerica.edu.ec",
        "insite.4cd.edu",
        "insite.4cd.edu",
        "institutomerani.edu.co",
        "int.edu.gr",
        "inu.edu.vn",
        "ipdbuu.com.cn",
        "isbstudent.comsats.edu.pk",
        "isctem.ac.mz",
        "ishikuniversity.net",
        "isik.edu.tr",
        "isise.edu.pe",
        "isise.edu.pe",
        "isiswa.uitm.edu.my",
        "iskolarngbayan.pup.edu.ph",
        "itca.edu.sv",
        "itculiacan.edu.mx",
        "itspozarica.edu.mx",
        "itstep.academy",
        "ittc.edu.vn",
        "itu.ac.tzbjtu.edu.cn",
        "itu.edu.tr",
        "iu.edu.jo",
        "ivytech.edu",
        "jfn.ac.lk",
        "jiangnan.edu.cn",
        "jic.edu.sa",
        "jlu.edu.cn",
        "jmpaneracollege.com",
        "jmu.edu.cn",
        "jou.edu.cn",
        "jsust.edu.cn",
        "jsut.edu.cn",
        "just.edu.jo",
        "k.kkk.ac.nz",
        "k.tut.edu.pl",
        "kafrelsheikh2.moe.edu.eg",
        "kangnam.ac.kr",
        "kashop.me",
        "kastamonu.edu.tr",
        "kbtc.edu.mm",
        "kbtut.tj",
        "kcl.ac.uk",
        "kfu.edu.cn",
        "kg.edu.kg",
        "khi.iba.edu.pk",
        "khugjil.edu.mn",
        "kings.ac.id",
        "kings.edu.uy",
        "kingshurst.ac.uk",
        "kjdx.ac.cn",
        "kkk.ac.nz",
        "kkk.school.nz",
        "kmismail.com",
        "kmitl.ac.th",
        "kmitl.ac.th",
        "kmust.edu.cn",
        "kmutt.ac.th",
        "knights.ucf.edu",
        "kodeklubbenflaa.no",
        "konkuk.ac.kr",
        "kps.edu.pk",
        "kps.edu.pk",
        "kst.edu.sg",
        "ksu.edu.bi",
        "kust.edu.cn",
        "kvsrodehradun.co.in",
        "kwiatek365.pl",
        "kyile.website",
        "lau.edu",
        "lawsonstate.edu",
        "lcu.edu.cn",
        "ldceahm.gujgov.edu.in",
        "leonvero.com",
        "lfnu.edu.cn",
        "liccsalsl.org",
        "lindenps.org",
        "link.tyut.edu.cn",
        "live",
        "live.mut.ac.za",
        "live.mut.ac.za",
        "live.unilag.edu.ng",
        "lixin.edu.cn",
        "ljb.edu.hk",
        "lonestar.edu",
        "losrios.edu",
        "lsdc.co.za",
        "lsdc.co.za",
        "lttc.edu.vn",
        "lucbjtu.ac.uk",
        "lumstu.com",
        "lxiv.secondary.edu.pl",
        "lzjtu.edu.cn",
        "lzpcc.edu.cn",
        "lzu.edu.cn",
        "m.fafu.edu.cn",
        "m.uno.edu.gr",
        "mackenzista.com.br",
        "madisoncollege.edu",
        "mahasiswa.itb.ac.id",
        "mahasiswa.itb.ac.id",
        "mail.0du.win",
        "mail.ac.id",
        "mail.alumni.edu.vn",
        "mail.apu.edu.my",
        "mail.aub.edu",
        "mail.bnuz.edu.cn",
        "mail.bnuz.edu.cn",
        "mail.broward.edu",
        "mail.ccmu.edu.cn",
        "mail.chzu.edu.cn",
        "mail.chzu.edu.cn",
        "mail.csu.edu.cn",
        "mail.davistech.edu",
        "mail.dhu.edu.cn",
        "mail.dream.edu.kg",
        "mail.edu.tw",
        "mail.escuelaing.edu.co",
        "mail.fmftsk.cn",
        "mail.hbut.edu.cn",
        "mail.hrka.net",
        "mail.icmbs.sch.id",
        "mail.imu.edu.cn",
        "mail.irsc.edu",
        "mail.lcc.edu",
        "mail.ltcc.edu",
        "mail.mss.sc.ug",
        "mail.mzr.me",
        "mail.ntust.edu.tw",
        "mail.nwpu.edu.cn",
        "mail.philau.edu",
        "mail.sbu.ac.ir",
        "mail.sjtu.edu.cn",
        "mail.smamuhammadiyahkotaternate.sch.id",
        "mail.stmikbumigora.ac.id",
        "mail.sustc.edu.cn",
        "mail.tdc.edu.vn",
        "mail.tmcc.edu",
        "mail.ucv.es",
        "mail.uic.edu.cn",
        "mail.umy.ac.id",
        "mail.wcccd.edu",
        "mail.wvncc.edu",
        "mail.xjtu.edu.cn",
        "mail.ypu.edu.tw",
        "mail2.gdut.edu.cn",
        "mailpoof.com",
        "mails.cust.edu.cn",
        "mails.hufe.edu.cn",
        "mails.imnu.edu.cn",
        "mails.jlu.edu.cn",
        "mails.mmnnsf.cn",
        "mails.qust.edu.cn",
        "mails.tsinghua.edu.cn",
        "mancheopenschool.fr",
        "maranatha.edu",
        "maricopa.edu",
        "masu.edu.cn",
        "matc.edu",
        "mbz.ens.sch.ae",
        "mcast.edu.mt",
        "mccd.edu",
        "mccmulund.ac.in",
        "mcl.edu.ph",
        "mclennan.edu",
        "mdu.edu.rs",
        "mdx.ac",
        "me.bergen.edu",
        "mec.edu.py",
        "mechnik.spb.ru",
        "medicine.zu.edu.eg",
        "meduca.edu.pa",
        "meduca.edu.pa",
        "mercubuana.ac.id",
        "mfk.app",
        "mgccc.edu",
        "mgt.sjp.ac.lk",
        "mhzayt.online",
        "miitt.space",
        "mined.edu.sv",
        "mitid.edu.in",
        "miucce.com",
        "mjj.edu.ge",
        "mju.ac.th",
        "mku.ac.ke",
        "ml",
        "modern-academy.edu.eg",
        "moe-dl.edu.my",
        "moe-dl.edu.my",
        "moej.edu.jo",
        "mohawkcollege.ca",
        "montgomerycollege.edu",
        "mooroolbarkcollege.vic.edu.au",
        "ms.daihocthudo.edu.vn",
        "ms.dendai.ac.jp",
        "ms.edu.tw",
        "ms.uas.edu.mx",
        "ms1.mcu.edu.tw",
        "msjc.edu",
        "mskh.am",
        "mso365.ulp.pt",
        "mu.edu.sa",
        "mubs.ac.ug",
        "muccobs.ac.tz",
        "mul.edu.pk",
        "must.edu.mn",
        "my.anokaramsey.edu",
        "my.barstow.edu",
        "my.bridgevalley.edu",
        "my.browncollege.edu",
        "my.canyons.edu",
        "my.ccri.edu",
        "my.centennialcollege.ca",
        "my.chamberlain.edu",
        "my.chattanoogastate.edu",
        "my.cleveland.edu",
        "my.edu.moi",
        "my.jccmi.edu",
        "my.lowercolumbia.edu",
        "my.riohondo.edu",
        "my.smccd.edu",
        "my.stchas.edu",
        "my.tccd.edu",
        "my.unitec.edu.mx",
        "my.uvm.edu.mx",
        "my.wgu.edu",
        "my.witcc.edu",
        "my.yosemite.edu",
        "mybac.ac.bw",
        "mycom.marin.edu",
        "mylife.unisa.ac.za",
        "mymail.aacc.edu",
        "mymail.gaston.edu",
        "mymail.mapua.edu.ph",
        "mymail.tcc.fl.edu",
        "myportal.taftcollege.edu",
        "myseneca.ca",
        "myunitec.com.mx",
        "mywvm.wvm.edu",
        "mziuri.edu.ge",
        "nankai.edu.cn",
        "navarrocollege.edu",
        "nbu.edu.cn",
        "nccu.edu.tw",
        "ncepu.cn",
        "ncepu.edu.cn",
        "ncepu.edu.cn",
        "ncist.edu.cn",
        "ncwu.edu.cn",
        "nenu.edu.cn",
        "nes.edu.jo",
        "neu.edu.vn",
        "nfs.edu.rs",
        "nic.edu",
        "nicu.ac.mu",
        "nihaomeimei.me",
        "ninja",
        "njau.edu.cn",
        "njit.edu",
        "njit.edu.cn",
        "njnu.edu.cn",
        "njtech.edu.cn",
        "nju.edu.cn",
        "nkdx.ac.cn",
        "nmjc.edu",
        "nmms-mautern.at",
        "nnu.edu.cn",
        "noc.edu",
        "northampton.edu",
        "northfacing.ac.cn",
        "northshore.edu",
        "northshore.edu",
        "noun.edu.ng",
        "noun.edu.ng",
        "npi.edu",
        "nttu.edu.vn",
        "ntu.edu.pk",
        "nu.ac.th",
        "nu.edu.eg",
        "nub.edu.eg",
        "nube.unadmexico.mx",
        "nuc.edu.cn",
        "nur.edu.bo",
        "nuv.ac.in",
        "nwafu.edu.cn",
        "nwfsc.edu",
        "nwosu.edu",
        "nxmu.edu.cn",
        "o365.msu.ac.th",
        "o365.unab.edu.co",
        "o6u.edu.eg",
        "obszeester.nl",
        "occc.edu",
        "ocgs.edu.ph",
        "off365.ncku.edu.tw",
        "office.aefc.edu.pt",
        "office.deu.ac.kr",
        "office.itb.ac.id",
        "office.stust.edu.tw",
        "office365.kunsan.ac.kr",
        "office365.ncu.edu.tw",
        "office365.nkust.edu.tw",
        "ofppt-edu.ma",
        "ogr.altinbas.edu.tr",
        "ogr.cu.edu.tr",
        "ogr.duzce.edu.tr",
        "ogrenci.bartin.edu.tr",
        "ogrenci.bartin.edu.tr",
        "ogrenci.bilecik.edu.tr",
        "ogrenci.karabuk.edu.tr",
        "os-bbuha.edu.me",
        "os-dkorac.edu.me",
        "osasmailovic.edu.ba",
        "oshs.edu.ba",
        "otp39.ru",
        "ouc.edu.cn",
        "outlook.rmutr.ac.th",
        "pace.edu",
        "palermo.edu",
        "palloimre.ro",
        "palomar.edu",
        "paofu.us",
        "parallax.lk",
        "paulsmiths.edu",
        "pcc.edu",
        "peking.pkumail.tech",
        "pekingwebmail.tech",
        "petkasem.ac.th",
        "pg.edu.pl",
        "pgc.edu.pk",
        "pharm.bsu.edu.eg",
        "philander.edu",
        "philips.edu.ar",
        "phuocbinh.edu.vn",
        "phyd.psu.edu.eg",
        "pipeline.sbcc.edu",
        "pises.edu.sa",
        "pisjes.edu.sa",
        "pkru.ac.th",
        "plm.edu.ph",
        "pme.suezuni.edu.eg",
        "pmu.edu.sa",
        "pom-ko.edu.me",
        "portal.uni.edu.ni",
        "post.eurasia.edu",
        "posta.mu.edu.tr",
        "posta.pau.edu.tr",
        "postgradoutp.edu.pe",
        "powerbi.edu.kg",
        "prc.ac.th",
        "profundity.com.tw",
        "psm.edu.ve",
        "psu.edu.eg",
        "puccampinas.edu.br",
        "puce.edu.ec",
        "pucese.edu.ec",
        "pucgo.edu.br",
        "pucmm.edu.do",
        "pucpr.edu.br",
        "puntlandstateuniversity.com",
        "pycharm.ac.cn",
        "qaliobia4.moe.edu.eg",
        "qhnu.edu.cn",
        "queens.ac.id",
        "qust.edu.cn",
        "qvtu.edu.cn",
        "qzit.edu.cn",
        "r4a-1.deped.gov.ph",
        "r4a-3.deped.gov.ph",
        "rangers.nwosu.edu",
        "rawafed.edu.ps",
        "rb.edu.ps",
        "rb.edu.ps",
        "rb.moe.gov.sa",
        "red.unid.mx",
        "rg.moe.gov.sa",
        "rhodesstate.edu",
        "riohondo.edu",
        "rittiya.ac.th",
        "rmu.ac.th",
        "rmuti.ac.th",
        "rmutl.ac.th",
        "rmutl.ac.th",
        "rmutto.ac.th",
        "rochester.edu",
        "rocks",
        "roxbury.edu",
        "ruhr-uni-bochum.de",
        "rule.edu.kh",
        "rupp.edu.kh",
        "rutgers.edu",
        "s.afeka.ac.il",
        "s.hlju.edu.cn",
        "s.slcupc.edu.cn",
        "s.unikl.edu.my",
        "s.upc.edu.cn",
        "saddleback.edu",
        "sandyupper.net",
        "sbcc.edu",
        "sbu.ac.ir",
        "sc.edu.my",
        "scc.stanly.edu",
        "sch.edu.af",
        "sch.moe.edu.eg",
        "school.mss.sc.ug",
        "schools.ac.cy",
        "scnu.edu.cn",
        "scnu.edu.cn",
        "scu.edu.cn",
        "scuec.edu.cn",
        "scun.edu.cn",
        "sdju.edu.cn",
        "sdnu.edu.cn",
        "sdu.edu.cn",
        "sdufe.edu.cn",
        "sdust.edu.cn",
        "sdut.edu.cn",
        "secupv.org",
        "sekaschool.ac.th",
        "sekuco.org",
        "sem.tsinghua.edu.cn",
        "sempreung.com.br",
        "sempreuninorte.com.br",
        "senacminas.edu.br",
        "senacsp.edu.br",
        "sencico.edu.pe",
        "seu.edu.cn",
        "seu.edu.mk",
        "sfcollege.edu",
        "sfu.edu.cn",
        "sg.edu.vn",
        "sh-eng.menofia.edu.eg",
        "sh-eng.menofia.edu.eg",
        "sharif.edu",
        "sharif.ir",
        "sharjah.ac.ae",
        "sharkia1.moe.edu.eg",
        "sharkia3.moe.edu.eg",
        "shisu.edu.cn",
        "shitac.tech",
        "shmtu.edu.cn",
        "shu.edu.cn",
        "si.edu",
        "sicau.edu.cn",
        "sierracollege.edu",
        "siit.edu.cn",
        "sinclair.edu",
        "siswa.email",
        "siswa.um.edu.my",
        "siswa365.um.edu.my",
        "sit.edu.cn",
        "sjbit.edu.in",
        "sjtu.edu.cn",
        "slc.ubc.ca",
        "slc.ubc.ca",
        "slc.ubc.ca",
        "slu.edu.ph",
        "sm.imamu.edu.sa",
        "smail.cczu.edu.cn",
        "smail.nju.edu.cn",
        "smail.skawi.me",
        "smakstmariamalang.sch.id",
        "smc.edu",
        "snnu.edu.cn",
        "soongsil.ac.kr",
        "soongsil.ac.kr",
        "sotcstudent.net",
        "southwest.tn.edu",
        "spscc.edu",
        "sss.edu.bi",
        "sstu-edu.ru",
        "ssuet.edu.pk",
        "st-bernards.slough.sch.uk",
        "st.btbu.edu.cn",
        "st.buh.edu.vn",
        "st.gxu.edu.cn",
        "st.maltepe.edu.tr",
        "st.nuc.edu.cn",
        "st.sandau.edu.cn",
        "st.schools.ac.cy",
        "st.uqu.edu.sa",
        "st.usst.edu.cn",
        "staff.pmm.edu.my",
        "staffs.sch.uk",
        "stchas.edu",
        "std.antalya.edu.tr",
        "std.aou.edu.eg",
        "std.balamand.edu.lb",
        "std.hu.edu.jo",
        "std.izu.edu.tr",
        "std.nisantasi.edu.tr",
        "std.uestc.edu.cn",
        "std.yildiz.edu.tr",
        "sti.edu.ph",
        "stikom-bali.ac.id",
        "stlcc.edu",
        "stmail.tanenbaumchat.org",
        "stou.ac.th",
        "stu.ahu.edu.cn",
        "stu.aydin.edu.tr",
        "stu.ccsu.edu.cn",
        "stu.cdsj6.edu.mo",
        "stu.cdsj6.edu.mo",
        "stu.cdut.edu.cn",
        "stu.centralaz.edu",
        "stu.cihanuniversity.org",
        "stu.colegiotorremalmuerta.es",
        "stu.cpu.edu.cn",
        "stu.cqupt.edu.cn",
        "stu.csust.edu.cn",
        "stu.ctcd.edu",
        "stu.cuz.edu.cn",
        "stu.ftccollege.edu",
        "stu.gzucm.edu.cn",
        "stu.haust.edu.cn",
        "stu.haut.edu.cn",
        "stu.hcnu.edu.cn",
        "stu.hit.edu.cn",
        "stu.hnie.edu.cn",
        "stu.hnucm.edu.cn",
        "stu.hrbust.edu.cn",
        "stu.hubu.edu.cn",
        "stu.jazanu.edu.sa",
        "stu.jiangnan.edu.cn",
        "stu.just.edu.cn",
        "stu.kemu.ac.ke",
        "stu.kust.edu.cn",
        "stu.liiajc.me",
        "stu.meu.edu.jo",
        "stu.meu.edu.jo",
        "stu.mju.edu.cn",
        "stu.mziuri.edu.ge",
        "stu.nchu.edu.cn",
        "stu.ncwu.edu.cn",
        "stu.nmu.edu.cn",
        "stu.nuc.edu",
        "stu.nun.edu.cn",
        "stu.parkland.edu",
        "stu.peihua.edu.cn",
        "stu.pim.ac.th",
        "stu.ptit.edu.vn",
        "stu.scau.edu.cn",
        "stu.scu.edu.cn",
        "stu.sdnu.edu.cn",
        "stu.shzu.edu.cn",
        "stu.sisu.edu.cn",
        "stu.sqxy.edu.cn",
        "stu.suse.edu.cn",
        "stu.sxau.edu.cn",
        "stu.sxit.edu.cn",
        "stu.tjcu.edu.cn",
        "stu.unizulu.ac.za",
        "stu.wxic.edu.cn",
        "stu.xhsysu.edu.cn",
        "stu.xhu.edu.cn",
        "stu.xjtu.edu.cn",
        "stu.xpu.edu.cn",
        "stu.yznu.cn",
        "stu.zjhu.edu.cn",
        "stu.zuel.edu.cn",
        "stud.acdt.edu.cn",
        "stud.tjut.edu.cn",
        "stud.ur.ac.rw",
        "student.aast.edu",
        "student.alamo.edu",
        "student.bahria.edu.pk",
        "student.bau.edu.lb",
        "student.cankaya.edu.tr",
        "student.carlalbert.edu",
        "student.ccp.edu",
        "student.cdsj.edu.mo",
        "student.chula.ac.th",
        "student.citruscollege.edu",
        "student.ciu.edu.tr",
        "student.cmccd.edu",
        "student.csn.edu",
        "student.cumtb.edu.cn",
        "student.cumtb.edu.cn",
        "student.eelu.edu.eg",
        "student.egcc.edu",
        "student.eur.nl",
        "student.glendale.edu",
        "student.hiu.vn",
        "student.hiu.vn",
        "student.huc.edu.vn",
        "student.huc.edu.vn",
        "student.humg.edu.vn",
        "student.hywoman.ac.kr",
        "student.isf.edu.hk",
        "student.istiqlal.sch.id",
        "student.ksu.edu.sa",
        "student.laccd.edu",
        "student.lccc.wy.edu",
        "student.lccc.wy.edu",
        "student.mahidol.ac.th",
        "student.maseno.ac.ke",
        "student.mercubuana.ac.id",
        "student.mksu.ac.ke",
        "student.mmarau.ac.ke",
        "student.monroecc.edu",
        "student.mseuf.edu.ph",
        "student.msjc.edu",
        "student.mtsac.edu",
        "student.napavalley.edu",
        "student.nibm.lk",
        "student.nocccd.edu",
        "student.northampton.edu",
        "student.oaklandcc.edu",
        "student.ohlone.edu",
        "student.olympic.edu",
        "student.owens.edu",
        "student.psis.edu.my",
        "student.ptithcm.edu.vn",
        "student.ptss.edu.my",
        "student.ptss.edu.my",
        "student.qau.edu.pk",
        "student.rockvalleycollege.edu",
        "student.sbccd.edu",
        "student.scalda.nl",
        "student.scf.edu",
        "student.sekolahanugrah.sch.id",
        "student.smanrandudongkal.sch.id",
        "student.smawirausaha.sch.id",
        "student.smc.edu",
        "student.tsu.edu.ph",
        "student.ub.ac.id",
        "student.uin-suka.ac.id",
        "student.uitm.edu.my",
        "student.uj.ac.za",
        "student.unicv.edu.cv",
        "student.universitaspertamina.ac.id",
        "student.uno-r.edu.ph",
        "student.unsw.edu.au",
        "student.utem.edu.my",
        "student.uum.edu.my",
        "student.wsb.edu.pl",
        "student.wstkt.edu.pl",
        "studenti.unical.it",
        "studenti.unimi.it",
        "students.cccti.edu",
        "students.fui.edu.pk",
        "students.fui.edu.pk",
        "students.hou.edu.vn",
        "students.jinan.edu.lb",
        "students.mohave.edu",
        "students.mu.ac.ke",
        "students.muet.edu.pk",
        "students.noc.edu",
        "students.prairiestate.edu",
        "students.prairiestate.edu",
        "students.ridgeway.herts.sch.uk",
        "students.rossu.edu",
        "students.smanra.sch.id",
        "students.solano.edu",
        "students.uajy.ac.id",
        "students.uettaxila.edu.pk",
        "students.ukdw.ac.id",
        "students.unilorin.edu.ng",
        "students.uwc.edu",
        "students.westerntc.edu",
        "studio",
        "stumail.hbu.edu.cn",
        "stumail.sdut.edu.cn",
        "stumail.sdut.edu.cn",
        "su.ac.th",
        "subr.edu",
        "subu.edu.tr",
        "suda.edu.cn",
        "sufe.edu.cn",
        "sunburysc.vic.edu.au",
        "sunydutchess.edu",
        "sus.edu",
        "sust.edu",
        "sust.edu.cn",
        "sv.hotec.edu.vn",
        "sv.ussh.edu.vn",
        "sv.ussh.edu.vn",
        "swccd.edu",
        "swccd.edu",
        "swpu.edu.cn",
        "swu.edu.cn",
        "sxlg.ac.cn",
        "sz.pku.edu.cn",
        "sziit.edu.cn",
        "t.edu.vn",
        "t.edu.vn",
        "t.odmail.cn",
        "taalim.ma",
        "tacomacc.edu",
        "tanta.edu.eg",
        "tau.usbmed.edu.co",
        "tbr.edu",
        "tcathartsville.edu",
        "tccd.edu",
        "tcl.edu",
        "tech",
        "tecmilenio.mx",
        "tese.edu.mx",
        "thcstranvangiau.com",
        "thebes.edu.eg",
        "thenyeripoly.ac.ke",
        "thpt-baria-brvt.edu.vn",
        "tijmu.edu.cn",
        "tjdx.ac.cn",
        "tju.edu.cn",
        "tk",
        "tmu.edu.cn",
        "tnw.ac.th",
        "tongji.edu.cn",
        "tp.edu.tw",
        "tralu.hdu.edu.cn",
        "traralsc.vic.edu.au",
        "tri-c.edu",
        "tse.moe.edu.eg",
        "tsinghua.pkumail.tech",
        "tu.edu.vn",
        "tulsacc.edu",
        "tum.ac.ke",
        "tusur.ru",
        "tut4life.ac.za",
        "tut4life.ac.za",
        "twzhhq.online",
        "uac.edu.co",
        "uac.edu.co",
        "uadec.edu.mx",
        "uam.edu.co",
        "uanl.edu.mx",
        "ub.ac.bw",
        "ub.edu.bs",
        "ubboemmius.nl",
        "ubp.edu.ar",
        "uca.edu.ar",
        "ucacue.edu.ec",
        "uce.edu.do",
        "uce.edu.ec",
        "ucp.edu.pk",
        "ucsiuniversity.edu.my",
        "ucsm.edu.pe",
        "ucsy.edu.mm",
        "udca.edu.co",
        "udenar.edu.co",
        "udla.edu.co",
        "ues.edu.sv",
        "ufhec.edu.do",
        "ufidelitas.ac.cr",
        "ufpa.br",
        "ufromail.cl",
        "ug.edu.ec",
        "uh.edu",
        "uiot.ac.ug",
        "uj.edu.sa",
        "ujs.edu.cn",
        "ul.edu.co",
        "ul.edu.lb",
        "ula.edu.mx",
        "ulbra.edu.br",
        "ulive.pccu.edu.tw",
        "um5.ac.ma",
        "umbc.edu",
        "umkt.ac.id",
        "ump.edu.my",
        "ump.edu.vn",
        "unach.edu.ec",
        "unadvirtual.edu.co",
        "unah.hn",
        "unasa.edu.sv",
        "unasam.edu.pe",
        "uncp.edu.pe",
        "une.edu",
        "unemi.edu.ec",
        "uni-muenster.de",
        "uniabuja.edu.ng",
        "uniacademia.edu.br",
        "unicda.edu.do",
        "unicoc.edu.co",
        "unifacs.edu.br",
        "unijos.edu.ng",
        "unilu.ac.cd",
        "unimaksl.education",
        "unimetroangola.com",
        "uniminuto.edu.co",
        "uninorte.edu.co",
        "unisalle.edu.co",
        "unisilvaner.info",
        "unisinu.edu.co",
        "unisinu.edu.co",
        "unitec.edu",
        "univ-annaba.org",
        "univ-caen.fr",
        "univalle.edu",
        "universidad-une.com",
        "universidad-une.com",
        "universidadean.edu.co",
        "unm.edu.pe",
        "uno.edu.gr",
        "uns.edu.pe",
        "unsl.edu.ar",
        "unwe.bg",
        "uoh.edu.pk",
        "uon.edu.au",
        "uopca.unipune.ac.in",
        "uopstd.edu.jo",
        "uotago.ac.nz",
        "up.ac.pa",
        "upc.edu.pe",
        "upeu.edu.pe",
        "upm.edu.my",
        "upsjb.edu.pe",
        "uraccan.edu.ni",
        "urgrad.rochester.edu",
        "url.edu.gt",
        "usg.edu",
        "usiu.ac.ke",
        "usms.ac.ma",
        "usst.edu.cn",
        "ust.hk",
        "ustabuca.edu.co",
        "ustb.edu.cn",
        "ustc.edu.cn",
        "uta.edu.ec",
        "utcancun.mx",
        "utch.edu.co",
        "ute.edu.mx",
        "utecnologica.edu.bo",
        "uteco.edu.do",
        "uteco.edu.do",
        "utexas.edu",
        "utmachala.edu.ec",
        "utp.ac.pa",
        "utp.edu.pe",
        "utpl.edu.ec",
        "uts.edu.ve",
        "uttab.edu.mx",
        "uv.edu.ph",
        "uy.edu.mm",
        "vaa.edu.vn",
        "vanlanguni.vn",
        "vcccd.edu",
        "vccs.edu",
        "viacesi.fr",
        "vict.edu.ht",
        "vief.edu.vn",
        "vikings.grayson.edu",
        "vinhuni.edu.vn",
        "vip.henu.edu.cn",
        "vip.hnist.edu.cn",
        "vit.edu.in",
        "vnu.edu.vn",
        "volmail.jalc.edu",
        "vsma.info",
        "vtdi.edu.jm",
        "wellsfargocomcardholders.com",
        "wgu.edu",
        "whitecaps.gc.edu",
        "whu.edu.cn",
        "wmoenglishacademy.co.in",
        "workschool.ca",
        "wru.vn",
        "wstkt.edu.pl",
        "wust.edu.cn",
        "wust.edu.cn",
        "wwcc.edu",
        "wwu.de",
        "www.90888.cc",
        "www.beijing101.com",
        "wxic.edu.cn",
        "wzu.edu.cn",
        "x.pycharm.ac.cn",
        "xavierengg.com",
        "xbdx.ac.cn",
        "xidian.edu.cn",
        "xinfu.ac.cn",
        "xingle.me",
        "xiyou.edu.cn",
        "xjdx.ac.cn",
        "xmu.edu.cn",
        "xs.hnit.edu.cn",
        "xupt.edu.cn",
        "xy.dlpu.edu.cn",
        "xy.hbuas.edu.cn",
        "xy.xujc.com",
        "xzyz.edu.cn",
        "yangtzeu.edu.cn",
        "yccd.edu",
        "yznu.edu.cn",
        "yzpc.edu.cn",
        "zanestate.edu",
        "zcmu.edu.cn",
        "ze-zha.com",
        "zetech.ac.ke",
        "zhaoqian.ninja",
        "zictcollege.com",
        "zjgsu.edu.cn",
        "zjnu.edu.cn",
        "zjsru.edu.cn",
        "zju.edu.cn",
        "zknu.edu.cn",
        "zu.edu.jo",
        "zucc.edu.cn",
        "zuel.edu.cn",
        "zut.edu.cn",
    ]
)
