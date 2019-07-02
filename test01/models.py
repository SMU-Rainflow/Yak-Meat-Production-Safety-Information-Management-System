from django.db import models

# Create your models here.

class Form1_1_1(models.Model):
    id1 = models.CharField("月份",max_length=100)
    id2 = models.CharField("样地",max_length=100)
    id3 = models.FloatField("水温（T）")
    id4 = models.FloatField("总溶解固体（TDS）")
    id5 = models.FloatField("土壤电导率（EC）")
    id6 = models.FloatField("pH")
    id7 = models.FloatField("溶解氧（DO）")
    id8 = models.FloatField("化学耗氧量（COD）")
    id9 = models.FloatField("生物耗氧量（BOD）")
    id10 = models.FloatField("氨氮（NH3-N）")
    id11 = models.FloatField("总氮（TN）")
    id12 = models.FloatField("总磷（TP）")
    id13 = models.FloatField("总硬度")
    id14 = models.FloatField("硫化物")
    id15 = models.FloatField("粪大肠菌群")
    id16 = models.FloatField("铬（Cr）")
    id17 = models.FloatField("铜（Cu）")
    id18 = models.FloatField("锌（Zn）")
    id19 = models.FloatField("砷（As）")
    id20 = models.FloatField("铅（Pb）")


    class Meta:
        verbose_name="放牧草地地表水有害因子"
        verbose_name_plural=verbose_name

class Form1_1_2(models.Model):
    id1 = models.CharField("监测日期",max_length=100)
    id2 = models.CharField("监测地点",max_length=100)
    id3 = models.FloatField("水温（T）")
    id4 = models.FloatField("总溶解固体（TDS）")
    id5 = models.FloatField("土壤电导率（EC）")
    id6 = models.FloatField("pH")
    id7 = models.FloatField("溶解氧（DO）")
    id8 = models.FloatField("化学耗氧量（COD）")
    id9 = models.FloatField("生物耗氧量（BOD）")
    id10 = models.FloatField("氨氮（NH3-N）")
    id11 = models.FloatField("总氮（TN）")
    id12 = models.FloatField("总磷（TP）")
    id13 = models.FloatField("总硬度")
    id14 = models.FloatField("硫化物")
    id15 = models.FloatField("粪大肠菌群")
    id16 = models.FloatField("铬（Cr）")
    id17 = models.FloatField("铜（Cu）")
    id18 = models.FloatField("锌（Zn）")
    id19 = models.FloatField("砷（As）")
    id20 = models.FloatField("铅（Pb）")

    class Meta:
        verbose_name="黑河区断流动水有害因子监测"
        verbose_name_plural=verbose_name

class Form2_1_1(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("月份",max_length=100)
    id3 = models.CharField("GPS样点",max_length=100)
    id4 = models.CharField("样品号",max_length=100)
    id5 = models.FloatField("铝（Al3961）")
    id6 = models.FloatField("砷（As1890）")
    id7 = models.FloatField("硼（B2089）")
    id8 = models.FloatField("硼（B2496）")
    id9 = models.FloatField("硼（B2497）")
    id10 = models.FloatField("钡（Ba4934）")
    id11 = models.FloatField("铍（Be2348）")
    id12 = models.FloatField("钙（Ca3179）")
    id13 = models.FloatField("镉（Cd2265）")
    id14 = models.FloatField("铂（Co2286）")
    id15 = models.FloatField("铂（Co2378）")
    id16 = models.FloatField("铬（Cr2835）")
    id17 = models.FloatField("铜（Cu3273）")
    id18 = models.FloatField("铁（Fe2382）")
    id19 = models.FloatField("铁（Fe2395）")
    id20 = models.FloatField("铁（Hg2599）")
    id21 = models.FloatField("汞（Hg1849）")
    id22 = models.FloatField("汞（Hg1942）")
    id23 = models.FloatField("钾（K7664）")
    id24 = models.FloatField("钾（K7698）")
    id25 = models.FloatField("镁（Mg2795）")
    id26 = models.FloatField("镁（Mg2802）")
    id27 = models.FloatField("镁（Mg2852）")
    id28 = models.FloatField("锰（Mn2605）")
    id29 = models.FloatField("钼（Mo2045）")
    id30 = models.FloatField("钠（Na5895）")
    id31 = models.FloatField("镍（Ni2316）")
    id32 = models.FloatField("磷（P1774）")
    id33 = models.FloatField("磷（P1782）")
    id34 = models.FloatField("铅（Pb1822）")
    id35 = models.FloatField("硒（Se1960）")
    id36 = models.FloatField("硅（Si2124）")
    id37 = models.FloatField("硅（Si2516）")
    id38 = models.FloatField("硅（Si2881）")
    id39 = models.FloatField("锡（Sn2429）")
    id40 = models.FloatField("锡（Sn2839）")
    id41 = models.FloatField("锶（Sr2152）")
    id42 = models.FloatField("锶（Sr2165）")
    id43 = models.FloatField("锶（Sr3464硅）")
    id44 = models.FloatField("钛（Ti3234）")
    id45 = models.FloatField("钛（Ti3361）")
    id46 = models.FloatField("钒（V2924）")
    id47 = models.FloatField("锌（Zn2062）")

    class Meta:
        verbose_name="牧草矿物质icp原始数据"
        verbose_name_plural=verbose_name

class Form2_1_2(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("月份",max_length=100)
    id3 = models.CharField("GPS样点",max_length=100)
    id4 = models.CharField("样品号",max_length=100)
    id5 = models.FloatField("铝（Al3961）")
    id6 = models.FloatField("砷（As1890）")
    id7 = models.FloatField("硼（B2089）")
    id8 = models.FloatField("硼（B2496）")
    id9 = models.FloatField("硼（B2497）")
    id10 = models.FloatField("钡（Ba4934）")
    id11 = models.FloatField("铍（Be2348）")
    id12 = models.FloatField("钙（Ca3179）")
    id13 = models.FloatField("镉（Cd2265）")
    id14 = models.FloatField("铂（Co2286）")
    id15 = models.FloatField("铂（Co2378）")
    id16 = models.FloatField("铬（Cr2835）")
    id17 = models.FloatField("铜（Cu3273）")
    id18 = models.FloatField("铁（Fe2382）")
    id19 = models.FloatField("铁（Fe2395）")
    id20 = models.FloatField("铁（Hg2599）")
    id21 = models.FloatField("汞（Hg1849）")
    id22 = models.FloatField("汞（Hg1942）")
    id23 = models.FloatField("钾（K7664）")
    id24 = models.FloatField("钾（K7698）")
    id25 = models.FloatField("镁（Mg2795）")
    id26 = models.FloatField("镁（Mg2802）")
    id27 = models.FloatField("镁（Mg2852）")
    id28 = models.FloatField("锰（Mn2605）")
    id29 = models.FloatField("钼（Mo2045）")
    id30 = models.FloatField("钠（Na5895）")
    id31 = models.FloatField("镍（Ni2316）")
    id32 = models.FloatField("磷（P1774）")
    id33 = models.FloatField("磷（P1782）")
    id34 = models.FloatField("铅（Pb1822）")
    id35 = models.FloatField("硒（Se1960）")
    id36 = models.FloatField("硅（Si2124）")
    id37 = models.FloatField("硅（Si2516）")
    id38 = models.FloatField("硅（Si2881）")
    id39 = models.FloatField("锡（Sn2429）")
    id40 = models.FloatField("锡（Sn2839）")
    id41 = models.FloatField("锶（Sr2152）")
    id42 = models.FloatField("锶（Sr2165）")
    id43 = models.FloatField("锶（Sr3464硅）")
    id44 = models.FloatField("钛（Ti3234）")
    id45 = models.FloatField("钛（Ti3361）")
    id46 = models.FloatField("钒（V2924）")
    id47 = models.FloatField("锌（Zn2062）")

    class Meta:
        verbose_name="水体矿物质icp原始数据"
        verbose_name_plural=verbose_name




class Form2_1_3(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("月份",max_length=100)
    id3 = models.CharField("GPS样点",max_length=100)
    id4 = models.CharField("样品号",max_length=100)
    id5 = models.FloatField("铝（Al3961）")
    id6 = models.FloatField("砷（As1890）")
    id7 = models.FloatField("硼（B2089）")
    id8 = models.FloatField("硼（B2496）")
    id9 = models.FloatField("硼（B2497）")
    id10 = models.FloatField("钡（Ba4934）")
    id11 = models.FloatField("铍（Be2348）")
    id12 = models.FloatField("钙（Ca3179）")
    id13 = models.FloatField("镉（Cd2265）")
    id14 = models.FloatField("铂（Co2286）")
    id15 = models.FloatField("铂（Co2378）")
    id16 = models.FloatField("铬（Cr2835）")
    id17 = models.FloatField("铜（Cu3273）")
    id18 = models.FloatField("铁（Fe2382）")
    id19 = models.FloatField("铁（Fe2395）")
    id20 = models.FloatField("汞（Hg1849）")
    id21 = models.FloatField("汞（Hg1942）")
    id22 = models.FloatField("钾（K7664）")
    id23 = models.FloatField("钾（K7698）")
    id24 = models.FloatField("镁（Mg2795）")
    id25 = models.FloatField("镁（Mg2802）")
    id26 = models.FloatField("镁（Mg2852）")
    id27 = models.FloatField("锰（Mn2605）")
    id28 = models.FloatField("钼（Mo2045）")
    id29 = models.FloatField("钠（Na5895）")
    id30 = models.FloatField("镍（Ni2316）")
    id31 = models.FloatField("磷（P1774）")
    id32 = models.FloatField("磷（P1782）")
    id33 = models.FloatField("铅（Pb1822）")
    id34 = models.FloatField("硒（Se1960）")
    id35 = models.FloatField("硅（Si2124）")
    id36 = models.FloatField("硅（Si2516）")
    id37 = models.FloatField("硅（Si2881）")
    id38 = models.FloatField("锡（Sn2429）")
    id39 = models.FloatField("锡（Sn2839）")
    id40 = models.FloatField("锶（Sr2152）")
    id41 = models.FloatField("锶（Sr2165）")
    id42 = models.FloatField("锶（Sr3464硅）")
    id43 = models.FloatField("钛（Ti3234）")
    id44 = models.FloatField("钛（Ti3361）")
    id45 = models.FloatField("钒（V2924）")
    id46 = models.FloatField("锌（Zn2062）")
    id47 = models.FloatField("汞（Hg2599）")

    class Meta:
        verbose_name="土壤矿物质icp原始数据"
        verbose_name_plural=verbose_name


class Form2_2_1(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("月份",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("经度")
    id5 = models.FloatField("纬度")
    id6 = models.FloatField("ph")
    id7 = models.FloatField("全氮g/kg")
    id8 = models.FloatField("水解性氮mg/kg")
    id9 = models.FloatField("有机物%")
    id10 = models.FloatField("有效磷（mg/kg)")
    id11 = models.FloatField("有效钾(mg/kg)")
    id12 = models.FloatField("全钾（g/kg）")
    id13 = models.FloatField("全磷(g/kg)")
    

    class Meta:
        verbose_name="土壤养分数据"
        verbose_name_plural=verbose_name


class Form3_1_1(models.Model):
    id1= models.CharField("序号",max_length=100)
    id2= models.CharField("养殖场",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("pH")


    class Meta:
        verbose_name="8个养殖场土壤pH值"
        verbose_name_plural=verbose_name


class Form3_1_2(models.Model):
    id1 = models.CharField("序号",max_length=100, null=True,blank=True)
    id2 = models.CharField("养殖场",max_length=100, null=True,blank=True)
    id3 = models.CharField("样品号",max_length=100, null=True,blank=True)
    id4 = models.FloatField("铝（Al3961）", null=True,blank=True)
    id5 = models.FloatField("砷（As1937）", null=True,blank=True)
    id6 = models.FloatField("硼（B2089）", null=True,blank=True)
    id7 = models.FloatField("钡（Ba4934）", null=True,blank=True)
    id8 = models.FloatField("钙（Ca1840）", null=True,blank=True)
    id9 = models.FloatField("镉（Cd2144）", null=True,blank=True)
    id10 = models.FloatField("钴（Co2378）", null=True,blank=True)
    id11 = models.FloatField("铬（Cr2843）", null=True,blank=True)
    id12 = models.FloatField("铜（Cu2247）", null=True,blank=True)
    id13 = models.FloatField("铁（Fe2395）", null=True,blank=True)
    id14 = models.FloatField("汞（Hg1942）", null=True,blank=True)
    id15 = models.FloatField("钾（K7698）", null=True,blank=True)
    id16 = models.FloatField("镁（Mg2802）", null=True,blank=True)
    id17 = models.FloatField("锰（Mn2939）", null=True,blank=True)
    id18 = models.FloatField("钼（Mo2045）", null=True,blank=True)
    id19 = models.FloatField("钠（Na5895）", null=True,blank=True)
    id20 = models.FloatField("镍（Ni2216）", null=True,blank=True)
    id21 = models.FloatField("磷（P1858）", null=True,blank=True)
    id22 = models.FloatField("铅（Pb1822）", null=True,blank=True)
    id23 = models.FloatField("铅（Pd3242）", null=True,blank=True)
    id24 = models.FloatField("铷（Rb4244）", null=True,blank=True)
    id25 = models.FloatField("硒（Se1960）", null=True,blank=True)
    id26 = models.FloatField("硅（Si2881）", null=True,blank=True)
    id27 = models.FloatField("锡（Sn1899）", null=True,blank=True)
    id28 = models.FloatField("锶（Sr4215）", null=True,blank=True)
    id29 = models.FloatField("钛（Ti3361）", null=True,blank=True)
    id30 = models.FloatField("铊（Tl1908）", null=True,blank=True)
    id31 = models.FloatField("钒（V2687）", null=True,blank=True)
    id32 = models.FloatField("锌（Zn2062）", null=True,blank=True)


    class Meta:
        verbose_name="8个养殖场土壤矿物质ICP原始数据"
        verbose_name_plural=verbose_name


class Form3_1_3(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("砷（As）")
    id5 = models.FloatField("镉（Cd）")
    id6 = models.FloatField("铬（Cr）")
    id7 = models.FloatField("铜（Cu）")
    id8 = models.FloatField("镍（Ni）")
    id9 = models.FloatField("铅（Pb）")

    class Meta:
        verbose_name="8个养殖场土壤重金属含量"
        verbose_name_plural=verbose_name


class Form3_2_1(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场 ",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("pH")


    class Meta:
        verbose_name="8个养殖场饮用水pH"
        verbose_name_plural=verbose_name



class Form3_2_2(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("铝（Al3961）")
    id5 = models.FloatField("砷（As1937）")
    id6 = models.FloatField("硼（B2089）")
    id7 = models.FloatField("钡（Ba4934）")
    id8 = models.FloatField("钙（Ca1840）")
    id9 = models.FloatField("镉（Cd2144）")
    id10 = models.FloatField("铂（Co2378）")
    id11 = models.FloatField("铬（Cr2843）")
    id12 = models.FloatField("铜（Cu2247）")
    id13 = models.FloatField("铁（Fe2395）")
    id14 = models.FloatField("汞（Hg1942）")
    id15 = models.FloatField("钾（K7698）")
    id16 = models.FloatField("镁（Mg2802）")
    id17 = models.FloatField("锰（Mn2939）")
    id18 = models.FloatField("钼（Mo2045）")
    id19 = models.FloatField("钠（Na5895）")
    id20 = models.FloatField("镍（Ni2216）")
    id21 = models.FloatField("磷（P1858）")
    id22 = models.FloatField("铅（Pb1822）")
    id23 = models.FloatField("钯(Pd3242)")
    id24 = models.FloatField("铷(Rb4244)")
    id25 = models.FloatField("硒（Se1960）")
    id26 = models.FloatField("硅（Si2881）")
    id27 = models.FloatField("锡（Sn1899）")
    id28 = models.FloatField("锶（Sr4215）")
    id29 = models.FloatField("钛（Ti3361）")
    id30 = models.FloatField("铊(Tl1908)")
    id31 = models.FloatField("钒（V2687）")
    id32 = models.FloatField("锌（Zn2062）")

    class Meta:
        verbose_name="8个养殖场饮用水矿物元素icp原始数据-ms"
        verbose_name_plural=verbose_name


class Form3_2_3(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("砷（As）")
    id5 = models.FloatField("铅（Pb）")
    id6 = models.FloatField("镉（Cd）")
    id7 = models.FloatField("铬（Cr）")
    id8 = models.FloatField("汞（Hg）")

    class Meta:
        verbose_name="8个养殖场饮用水重金属含量"
        verbose_name_plural=verbose_name


class Form3_3_1(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("精料")
    id5 = models.FloatField("玉米秸")
    id6 = models.FloatField("酒糟")
    class Meta:
        verbose_name="8个养殖场饲料AFB1含量"
        verbose_name_plural=verbose_name


class Form3_3_2(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("精料")
    id5 = models.FloatField("玉米秸")
    id6 = models.FloatField("酒糟")

    class Meta:
        verbose_name="8个养殖场饲料克伦特罗含量"
        verbose_name_plural=verbose_name


class Form3_3_3(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("样品号",max_length=100)
    id4 = models.FloatField("精料")
    id5 = models.FloatField("玉米秸")
    id6 = models.FloatField("酒糟")

    class Meta:
        verbose_name="8个养殖场饲料莱克多巴胺含量                     "
        verbose_name_plural=verbose_name


class Form3_3_4(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("饲料",max_length=100)
    id4 = models.CharField("样品号",max_length=100)
    id5 = models.FloatField("样品重量")
    id6 = models.FloatField("铝（Al3961）")
    id7 = models.FloatField("砷（As1937）")
    id8 = models.FloatField("硼（B2089）")
    id9 = models.FloatField("钡（Ba4934）")
    id10 = models.FloatField("钙（Ca1840）")
    id11 = models.FloatField("镉（Cd2144）")
    id12 = models.FloatField("钴（Co2378）")
    id13 = models.FloatField("铬（Cr2843）")
    id14 = models.FloatField("铜（Cu2247）")
    id15 = models.FloatField("铁（Fe2395）")
    id16 = models.FloatField("汞（Hg1942）")
    id17 = models.FloatField("钾（K7698）")
    id18 = models.FloatField("镁（Mg2802）")
    id19 = models.FloatField("锰（Mn2939）")
    id20 = models.FloatField("钼（Mo2045）")
    id21 = models.FloatField("钠（Na5895）")
    id22 = models.FloatField("镍（Ni2216）")
    id23 = models.FloatField("磷（P1858）")
    id24 = models.FloatField("铅（Pb1822）")
    id25 = models.FloatField("钯（Pd3242）")
    id26 = models.FloatField("铷（Rb4244）")
    id27 = models.FloatField("硒（Se1960）")
    id28 = models.FloatField("硅（Si2881）")
    id29 = models.FloatField("锡（Sn1899）")
    id30 = models.FloatField("锶（Sr4215）")
    id31 = models.FloatField("钛（Ti3361）")
    id32 = models.FloatField("铊（Tl1908）")
    id33 = models.FloatField("钒（V2687）")
    id34 = models.FloatField("锌（Zn2062）")

    class Meta:
        verbose_name="8个养殖场饲料重金属元素icp原始数据"
        verbose_name_plural=verbose_name



class Form3_3_5(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("饲料",max_length=100)
    id4 = models.CharField("样品号",max_length=100)
    id5 = models.FloatField("砷（As）")
    id6 = models.FloatField("铅（Pb）")
    id7 = models.FloatField("镉（Cd）")
    id8 = models.FloatField("铬（Cr）")
    id9 = models.FloatField("铜（Cu）")
    id10 = models.FloatField("镍（Ni）")
    class Meta:
        verbose_name="8个养殖场饲料重金属元素含量"
        verbose_name_plural=verbose_name



class Form3_4_1(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("牛号",max_length=100)
    id4 = models.CharField("样品号",max_length=100)
    id5 = models.CharField("组织",max_length=100)
    id6 = models.FloatField("重量/g")
    id7 = models.FloatField("砷（As1937）")
    id8 = models.FloatField("铅（Pb1822）")
    id9 = models.FloatField("汞（Hg1942）")
    id10 = models.FloatField("镉（Cd2144）")
    id11 = models.FloatField("铬（Cr2843）")
    id12 = models.FloatField("铜（Cu2247）")
    id13 = models.FloatField("钴（Co2378）")
    id14 = models.FloatField("镍（Ni2216）")
    
    class Meta:
        verbose_name="8个养殖场牦牛组织矿物质icp原始数据"
        verbose_name_plural=verbose_name



class Form3_4_2(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("组织名称",max_length=100)
    id4 = models.CharField("样品号",max_length=100)
    id5 = models.FloatField("克伦特罗含量（μg/kg）")
    id6 = models.FloatField("莱克多巴胺含量（μg/kg）")

    class Meta:
        verbose_name="8个养殖场牦牛组织瘦肉精检测"
        verbose_name_plural=verbose_name



class Form3_4_3(models.Model):
    id1 = models.CharField("序号",max_length=100)
    id2 = models.CharField("养殖场",max_length=100)
    id3 = models.CharField("牛号",max_length=100)
    id4 = models.CharField("样品号",max_length=100)
    id5 = models.CharField("组织",max_length=100)
    id6 = models.FloatField("砷（As1937）")
    id7 = models.FloatField("铅（Pb1822）")
    id8 = models.FloatField("镉（Cd2144）")
    id9 = models.FloatField("铬（Cr2843）")
    id10 = models.FloatField("铜（Cu2247）")
    id11 = models.FloatField("钴（Co2378）")
    id12 = models.FloatField("镍（Ni2216）")

    class Meta:
        verbose_name="8个养殖场牦牛组织重金属含量"
        verbose_name_plural=verbose_name



class Form4_1_1(models.Model):
    id1 = models.CharField("季节",max_length=100)
    id2 = models.CharField("类型",max_length=100)
    id3 = models.CharField("测定时间",max_length=100)
    id4 = models.FloatField("气温第一天")
    id5 = models.FloatField("气温第二天")
    id6 = models.FloatField("气温第三天")
    id7 = models.FloatField("湿度第一天")
    id8 = models.FloatField("湿度第二天")
    id9 = models.FloatField("湿度第三天")
    id10 = models.FloatField("NH3第一天")
    id11 = models.FloatField("NH3第二天")
    id12 = models.FloatField("NH3第三天")
    id13 = models.FloatField("PM10第一天")
    id14 = models.FloatField("PM10第二天")
    id15 = models.FloatField("PM10第三天")

    class Meta:
        verbose_name="牦牛舍变化数据"
        verbose_name_plural=verbose_name



class Form5_1_1(models.Model):
    id1 = models.CharField("样品号",max_length=100)
    id2 = models.FloatField("AFB1(µg·kg-1)")
    id3 = models.FloatField("氨氮浓度NH3-H（mg·dL-1）")
    id4 = models.FloatField("挥发性脂肪酸VFA（mmol·L-1）")
    id5 = models.FloatField("乙酸Acetate（mmol·L-1）")
    id6 = models.FloatField("丙酸Propionate（mmol·L-1）")
    id7 = models.FloatField("乙丙比Acetate/Propionate")
    id8 = models.FloatField("丁酸Butyrate（mmol·L-1）")
    id9 = models.FloatField("戊酸Valerate（mmol·L-1）")
    id10 = models.FloatField("乳酸含量Lactate（mg·100mL-1）")
    id11 = models.FloatField("微晶纤维素酶活性Avicelase（U）")
    id12 = models.FloatField("羧甲基纤维素酶活性CMCase（U）")
    id13 = models.FloatField("纤维二糖酶活性Cellorbiase（U）")
    id14 = models.FloatField("木聚糖酶活性Xylanese（U）")
    id15 = models.FloatField("微生物蛋白MCP（mg·mL-1）")
    id16 = models.FloatField("瘤胃液AFB1(µg·L-1)")

    class Meta:
        verbose_name="黄曲酶素对牦牛瘤胃挥发性脂肪酸及纤维分解酶的影响"
        verbose_name_plural=verbose_name


class Form5_1_2(models.Model):
    id1 = models.CharField("样品号",max_length=100)
    id2 = models.FloatField("AFB1(µg·kg-1)")
    id3 = models.FloatField("Fe")
    id4 = models.FloatField("Cu")
    id5 = models.FloatField("Zn")
    id6 = models.FloatField("Mn")
    id7 = models.FloatField("Cr")
    id8 = models.FloatField("Se")
    id9 = models.FloatField("Ni")
    id10 = models.FloatField("Mo")
    id11 = models.FloatField("Sn")
    id12 = models.FloatField("Si")
    id13 = models.FloatField("Sr")
    id14 = models.FloatField("B")
    id15 = models.FloatField("As")
    id16 = models.FloatField("Pb")
    id17 = models.FloatField("Cd")
    id18 = models.FloatField("挥发性脂肪酸总量")
    id19 = models.FloatField("乙酸")
    id20 = models.FloatField("丙酸")
    id21 = models.FloatField("乙丙比")
    id22 = models.FloatField("丁酸")
    id23 = models.FloatField("戊酸")

    class Meta:
        verbose_name="黄曲酶素对牦牛瘤胃液矿物元素及挥发性脂肪酸的影响"
        verbose_name_plural=verbose_name



class Form5_1_3(models.Model):
    id1 = models.CharField("样品号",max_length=100)
    id2 = models.FloatField("AFB1(µg·kg-1)")
    id3 = models.FloatField("谷草转氨酶AST/(IU·L-1)")
    id4 = models.FloatField("谷丙转氨酶ALT/(IU·L-1)")
    id5 = models.FloatField("白蛋白ALB/(g·L-1)")
    id6 = models.FloatField("碱性磷酸酶ALP/(IU·L-1)")
    id7 = models.FloatField("乳酸脱氢酶LDH/(IU·L-1)")
    id8 = models.FloatField("谷氨酰氨基转移酶(IU·L-1)")
    id9 = models.FloatField("总胆汁酸(μmol·L-1)")
    id10 = models.FloatField("AFM1(µg·L-1)")

    class Meta:
        verbose_name="黄曲酶素对牦牛血清生化指标的影响"
        verbose_name_plural=verbose_name
