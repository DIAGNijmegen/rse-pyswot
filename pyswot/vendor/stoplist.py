# From https://github.com/JetBrains/swot.git@38c46e53

STOPLIST = frozenset(
    [
        "2020.gsm.cocite.pt",
        "90888.cc",
        "aaedu.edu.pl",
        "abcda.tech",
        "ahlg.ac.cn",
        "ahzyygz.edu.cn",
        "al.insper.edu.br",
        "alu.comillas.edu",
        "alu.fudan.edu.cn",
        "alum.ccu.edu.tw",
        "alum.urmc.rochester.edu",
        "alumni.albany.edu",
        "alumni.cmu.edu",
        "alumni.edu.vn",
        "alumni.montclair.edu",
        "alumni.nottingham.ac.uk",
        "alumni.sjtu.edu.cn",
        "alumni.unc.edu",
        "alumni.usp.br",
        "alumni.vcu.edu",
        "america.edu",
        "anadolu.edu.tr",
        "app",
        "apus.edu",
        "art.edu.lv",
        "asu.edu",
        "aufe.edu.cn",
        "aurora.ekof.bg.ac.rs",
        "australia.edu",
        "ayit.edu.cn",
        "azwestern.edu",
        "bbc.edu.cn",
        "bcmail.cuny.edu",
        "bese.ac.cn",
        "bestlistbase.com",
        "bfsu.edu.cn",
        "bgu.edu.kg",
        "bit.edu.cn",
        "bitzh.edu.cn",
        "bjdx.ac.cn",
        "bjlg.ac.cn",
        "bjtu.edu.cn",
        "bnu.edu.cn",
        "boscuos.com",
        "bucea.edu.cn",
        "caa.columbia.edu",
        "caa.edu.cn",
        "californiacolleges.edu",
        "campus.mccd.edu",
        "cau.edu.cn",
        "cc.peralta.edu",
        "ccc.edu",
        "cccd.edu",
        "ccnu.edu.cn",
        "ccsf.edu",
        "ccu.edu.tw",
        "cczu.edu.cn",
        "cdmc.edu.cn",
        "cet.edu",
        "cf",
        "chasefreedomactivate.com",
        "chc.edu.tw",
        "chd.edu.cn",
        "cheoa.studio",
        "cihanuniversity.org",
        "cjlu.edu.cn",
        "clatsopcc.edu",
        "cloudlearn.tech",
        "cmail.cornell.edu",
        "cochise.edu",
        "cocite.pt",
        "codesra.cn",
        "colegiotorremalmuerta.es",
        "collin.edu",
        "connect.hku.hk",
        "correo.icesi.edu.co",
        "cougarmail.collin.edu",
        "cpcc.edu",
        "cqu.edu.cn",
        "csu.ph",
        "ctgu.edu.cn",
        "cug.edu.cn",
        "cumt.edu.cn",
        "cumtb.edu.cn",
        "cuu.ac.ug",
        "davidsonccc.edu",
        "dcic.me",
        "deltacollege.edu",
        "dhu.edu.cn",
        "dlut.edu.cn",
        "dnmd.fun",
        "dragons.hutchcc.edu",
        "dxss.ac.cn",
        "dzxy.ntu.edu.cn",
        "eafit.edu.co",
        "eastafricauniversity.net",
        "ecupl.edu.cn",
        "ecust.edu.cn",
        "edu.icoremail.net",
        "edu.moi",
        "edu.tanta.edu.eg",
        "edu.uca.ma",
        "edu.umi.ac.ma",
        "educn.ac.cn",
        "email",
        "email.axc.edu.gr",
        "email.t.edu.vn",
        "emlmuak.cn",
        "enayu.com",
        "esore.asia",
        "esprims.tn",
        "eufe.edu.ht",
        "eurasia.edu",
        "everettcc.edu",
        "fjys.edu.cn",
        "fountaingatesc.vic.edu.au",
        "freenet.kg",
        "freenet.kg",
        "ga",
        "gduf.edu.cn",
        "ghazanthemprep.org",
        "giant.cos.edu",
        "go.edu.tw",
        "go.minnstate.edu",
        "go.sfcollege.edu",
        "gq",
        "graduate.hku.hk",
        "gsm.cocite.pt",
        "gsuite.cornell.edu",
        "gydx.ac.cn",
        "gzhtcm.edu.cn",
        "gzhu.edu.cn",
        "hainanu.edu.cn",
        "hainu.edu.cn",
        "haust.edu.cn",
        "haywood.edu",
        "hbdx.ac.cn",
        "hbu.edu.cn",
        "hbut.edu.cn ",
        "hc.edu.tw",
        "hcc.edu.tw",
        "hcmup.edu.vn",
        "henu.edu.cn",
        "hhu.edu.cn",
        "hiast.edu.vn",
        "hndx.ac.cn",
        "hnit.ed.cn",
        "hnu.edu.cn",
        "hqu.edu.cn",
        "hrbeu.edu.cn",
        "hstu.info",
        "huanghuai.edu.cn",
        "hubu.edu.cn",
        "hufe.edu.cn",
        "huse.edu.cn",
        "hust.edu.cn",
        "hznu.edu.cn",
        "icamtech.com",
        "iga-marrakech.ma",
        "imghost.tech",
        "imnu.edu.cn",
        "insite.4cd.edu",
        "int.edu.gr",
        "ipdbuu.com.cn",
        "ishikuniversity.net",
        "itu.ac.tzbjtu.edu.cn",
        "jiangnan.edu.cn",
        "jlu.edu.cn",
        "jmu.edu.cn",
        "jou.edu.cn",
        "jsust.edu.cn",
        "jsut.edu.cn",
        "k.kkk.ac.nz",
        "k.tut.edu.pl",
        "kashop.me",
        "kbtut.tj",
        "kg.edu.kg",
        "khi.iba.edu.pk",
        "kings.ac.id",
        "kings.edu.uy",
        "kjdx.ac.cn",
        "kkk.ac.nz",
        "kkk.school.nz",
        "kmismail.com",
        "kmust.edu.cn",
        "kst.edu.sg",
        "kust.edu.cn",
        "kyile.website",
        "leonvero.com",
        "lfnu.edu.cn",
        "live",
        "lixin.edu.cn",
        "ljb.edu.hk",
        "losrios.edu",
        "lucbjtu.ac.uk",
        "lxiv.secondary.edu.pl",
        "lzjtu.edu.cn",
        "lzpcc.edu.cn",
        "lzu.edu.cn",
        "m.fafu.edu.cn",
        "m.uno.edu.gr",
        "madisoncollege.edu",
        "mail.0du.win",
        "mail.ac.id",
        "mail.alumni.edu.vn",
        "mail.broward.edu",
        "mail.csu.edu.cn",
        "mail.davistech.edu",
        "mail.dhu.edu.cn",
        "mail.dream.edu.kg",
        "mail.edu.tw",
        "mail.fmftsk.cn",
        "mail.hbut.edu.cn",
        "mail.hrka.net",
        "mail.irsc.edu",
        "mail.ltcc.edu",
        "mail.mss.sc.ug",
        "mail.mzr.me",
        "mail.ntust.edu.tw",
        "mail.nwpu.edu.cn",
        "mail.philau.edu",
        "mail.sbu.ac.ir",
        "mail.sjtu.edu.cn",
        "mail.sustc.edu.cn",
        "mail.uic.edu.cn",
        "mail.wcccd.edu",
        "mail.xjtu.edu.cn",
        "mail2.gdut.edu.cn",
        "mailpoof.com",
        "mails.cust.edu.cn",
        "mails.hufe.edu.cn",
        "mails.imnu.edu.cn",
        "mails.mmnnsf.cn",
        "mails.qust.edu.cn",
        "mails.tsinghua.edu.cn",
        "masu.edu.cn",
        "mccd.edu",
        "mclennan.edu",
        "mdu.edu.rs",
        "me.bergen.edu",
        "mechnik.spb.ru",
        "mgccc.edu",
        "mgt.sjp.ac.lk",
        "mhzayt.online",
        "miitt.space",
        "miucce.com",
        "mjj.edu.ge",
        "ml",
        "ms.edu.tw",
        "msjc.edu",
        "my.anokaramsey.edu",
        "my.browncollege.edu",
        "my.canyons.edu",
        "my.ccri.edu",
        "my.chattanoogastate.edu",
        "my.cleveland.edu",
        "my.edu.moi",
        "my.jcu.edu.au",
        "my.riohondo.edu",
        "my.smccd.edu",
        "my.tccd.edu",
        "my.unitec.edu.mx",
        "my.yosemite.edu",
        "mycom.marin.edu",
        "mymail.aacc.edu",
        "mymail.gaston.edu",
        "mymail.tcc.fl.edu",
        "myportal.taftcollege.edu",
        "myunitec.com.mx",
        "mywvm.wvm.edu",
        "mziuri.edu.ge",
        "nbu.edu.cn",
        "nccu.edu.tw",
        "ncepu.cn",
        "ncepu.edu.cn",
        "ncist.edu.cn",
        "ncwu.edu.cn",
        "nenu.edu.cn",
        "nfs.edu.rs",
        "nicu.ac.mu",
        "nihaomeimei.me",
        "ninja",
        "njau.edu.cn",
        "njnu.edu.cn",
        "nju.edu.cn",
        "nkdx.ac.cn",
        "nnu.edu.cn",
        "noc.edu",
        "northfacing.ac.cn",
        "nuc.edu.cn",
        "nwafu.edu.cn",
        "nxmu.edu.cn",
        "occc.edu",
        "otp39.ru",
        "ouc.edu.cn",
        "palomar.edu",
        "paofu.us",
        "paulsmiths.edu",
        "peking.pkumail.tech",
        "pekingwebmail.tech",
        "pipeline.sbcc.edu",
        "post.eurasia.edu",
        "pycharm.ac.cn",
        "qhnu.edu.cn",
        "queens.ac.id",
        "qust.edu.cn",
        "rawafed.edu.ps",
        "riohondo.edu",
        "rochester.edu",
        "rocks",
        "rutgers.edu",
        "s.upc.edu.cn",
        "saddleback.edu",
        "sbcc.edu",
        "sbu.ac.ir",
        "scc.stanly.edu",
        "sch.edu.af",
        "school.mss.sc.ug",
        "scnu.edu.cn",
        "scu.edu.cn",
        "scuec.edu.cn",
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
        "seu.edu.cn",
        "seu.edu.mk",
        "sfu.edu.cn",
        "sharif.edu",
        "sharif.ir",
        "sharkia3.moe.edu.eg",
        "shisu.edu.cn",
        "shitac.tech",
        "shmtu.edu.cn",
        "shu.edu.cn",
        "si.edu",
        "sicau.edu.cn",
        "sierracollege.edu",
        "siit.edu.cn",
        "siswa.email",
        "sit.edu.cn",
        "sjtu.edu.cn",
        "smail.hunnu.edu.cn",
        "smail.nju.edu.cn",
        "smail.skawi.me",
        "smc.edu",
        "snnu.edu.cn",
        "sotcstudent.net",
        "southwest.tn.edu",
        "sss.edu.bi",
        "sstu-edu.ru",
        "st.btbu.edu.cn",
        "st.buh.edu.vn",
        "st.sandau.edu.cn",
        "st.usst.edu.cn",
        "std.uestc.edu.cn",
        "stlcc.edu",
        "stmail.tanenbaumchat.org",
        "stu.ahu.edu.cn",
        "stu.ccsu.edu.cn",
        "stu.centralaz.edu",
        "stu.cihanuniversity.org",
        "stu.colegiotorremalmuerta.es",
        "stu.cpu.edu.cn",
        "stu.cqupt.edu.cn",
        "stu.ctcd.edu",
        "stu.cuz.edu.cn",
        "stu.gzucm.edu.cn",
        "stu.haust.edu.cn",
        "stu.haut.edu.cn",
        "stu.hcnu.edu.cn",
        "stu.hit.edu.cn",
        "stu.hnie.edu.cn",
        "stu.hnucm.edu.cn",
        "stu.hubu.edu.cn",
        "stu.jiangnan.edu.cn",
        "stu.just.edu.cn",
        "stu.kust.edu.cn",
        "stu.liiajc.me",
        "stu.mziuri.edu.ge",
        "stu.ncwu.edu.cn",
        "stu.nmu.edu.cn",
        "stu.nun.edu.cn",
        "stu.parkland.edu",
        "stu.peihua.edu.cn",
        "stu.scau.edu.cn",
        "stu.scu.edu.cn",
        "stu.sdnu.edu.cn",
        "stu.shzu.edu.cn",
        "stu.sisu.edu.cn",
        "stu.sqxy.edu.cn",
        "stu.sxit.edu.cn",
        "stu.t.edu.vn",
        "stu.wxic.edu.cn",
        "stu.xhsysu.edu.cn",
        "stu.xpu.edu.cn",
        "stu.zuel.edu.cn",
        "stud.acdt.edu.cn",
        "student.alamo.edu",
        "student.carlalbert.edu",
        "student.cccs.edu",
        "student.citruscollege.edu",
        "student.ciu.edu.tr",
        "student.cmccd.edu",
        "student.cumtb.edu.cn",
        "student.glendale.edu",
        "student.humg.edu.vn",
        "student.ksu.edu.sa",
        "student.laccd.edu",
        "student.msjc.edu",
        "student.mtsac.edu",
        "student.napavalley.edu",
        "student.nocccd.edu",
        "student.ntu.edu.pk",
        "student.oaklandcc.edu",
        "student.ohlone.edu",
        "student.ptithcm.edu.vn",
        "student.rockvalleycollege.edu",
        "student.sbccd.edu",
        "student.scf.edu",
        "student.smc.edu",
        "student.unsw.edu.au",
        "student.wstkt.edu.pl",
        "students.cccti.edu",
        "students.noc.edu",
        "students.rossu.edu",
        "students.smanra.sch.id",
        "students.solano.edu",
        "students.uwc.edu",
        "students.westerntc.edu",
        "studio",
        "stumail.sdut.edu.cn",
        "subr.edu",
        "suda.edu.cn",
        "sufe.edu.cn",
        "sunydutchess.edu",
        "sus.edu",
        "sust.edu",
        "swccd.edu",
        "swpu.edu.cn",
        "swu.edu.cn",
        "sxlg.ac.cn",
        "sz.pku.edu.cn",
        "t.edu.vn",
        "t.odmail.cn",
        "tccd.edu",
        "tech",
        "tijmu.edu.cn",
        "tjdx.ac.cn",
        "tju.edu.cn",
        "tk",
        "tmu.edu.cn",
        "tongji.edu.cn",
        "tp.edu.tw",
        "tri-c.edu",
        "tse.moe.edu.eg",
        "tsinghua.pkumail.tech",
        "twzhhq.online",
        "uiot.ac.ug",
        "ujs.edu.cn",
        "ul.edu.lb",
        "unijos.edu.ng",
        "unimetroangola.com",
        "unisilvaner.info",
        "uno.edu.gr",
        "uotago.ac.nz",
        "usst.edu.cn",
        "ust.hk",
        "ustb.edu.cn",
        "ustc.edu.cn",
        "vanlanguni.vn",
        "vcccd.edu",
        "vccs.edu",
        "vict.edu.ht",
        "vip.henu.edu.cn",
        "vip.hnist.edu.cn",
        "volmail.jalc.edu",
        "wellsfargocomcardholders.com",
        "whu.edu.cn",
        "wru.vn",
        "wstkt.edu.pl",
        "wust.edu.cn",
        "www.90888.cc",
        "wxic.edu.cn",
        "wzu.edu.cn",
        "x.pycharm.ac.cn",
        "xbdx.ac.cn",
        "xidian.edu.cn",
        "xinfu.ac.cn",
        "xingle.me",
        "xiyou.edu.cn",
        "xjdx.ac.cn",
        "xmu.edu.cn",
        "xs.hnit.edu.cn",
        "xupt.edu.cn",
        "xzyz.edu.cn",
        "yangtzeu.edu.cn",
        "yccd.edu",
        "yzpc.edu.cn",
        "zanestate.edu",
        "zcmu.edu.cn",
        "ze-zha.com",
        "zhaoqian.ninja",
        "zictcollege.com",
        "zjgsu.edu.cn",
        "zjnu.edu.cn",
        "zjsru.edu.cn",
        "zju.edu.cn",
        "zknu.edu.cn",
        "zucc.edu.cn",
        "zuel.edu.cn",
        "zut.edu.cn",
    ]
)