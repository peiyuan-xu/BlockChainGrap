from bs4 import BeautifulSoup

html = """
<div id="tx-350367898" class="txdiv"><table class="table table-striped" cellpadding="0" cellspacing="0" style="padding:0px;float:left;margin:0px;width:100%"><tbody><tr><th colspan="3" align="left"><a class="hash-link" href="/tx/5f135757638ed739b801b5136be2ea8b790e987160eaf70450f701681f6c0d05">5f135757638ed739b801b5136be2ea8b790e987160eaf70450f701681f6c0d05</a> <span class="pull-right">2018-05-25 02:44:34</span></th></tr><tr><td class="txtd hidden-phone mobile-f12 stack-mobile"><a href="/address/1AwSG5UBrh3orJET2ewDbPP6viVqgm58uJ">1AwSG5UBrh3orJET2ewDbPP6viVqgm58uJ</a><br><a href="/address/13V5tYyfAytqUuYT7bP5LUpA1RPtcTVSse">13V5tYyfAytqUuYT7bP5LUpA1RPtcTVSse</a><br><a href="/address/1Nb1VDCjeKPAQswY6Qu2S71Lw9tbTzAkm9">1Nb1VDCjeKPAQswY6Qu2S71Lw9tbTzAkm9</a><br><a href="/address/19AvqPeUSGSbi7mXJnTKZXtVh9Q7aEa2Y7">19AvqPeUSGSbi7mXJnTKZXtVh9Q7aEa2Y7</a><br><a href="/address/16pcQiFBdx3PQ5dXegGoFWVxmreFQEsETQ">16pcQiFBdx3PQ5dXegGoFWVxmreFQEsETQ</a><br><a href="/address/12AHf3t87MGQiwa6Kx1K8H1iTtKhXu6dww">12AHf3t87MGQiwa6Kx1K8H1iTtKhXu6dww</a><br><a href="/address/188aDDbwyU6H5PmHFuuMGRt9CU1STNozG5">188aDDbwyU6H5PmHFuuMGRt9CU1STNozG5</a><br></td><td class="hidden-phone tx-arrow-col"><img src="/Resources/arrow_right_green.png"></td><td class="txtd mobile-f12 stack-mobile"><a href="/address/1GCFWHkg8mUUWNbk2JGk9QXmU7YTd8ypAi">1GCFWHkg8mUUWNbk2JGk9QXmU7YTd8ypAi</a> <span class="pull-right hidden-phone"><span data-c="6643000" data-time="1527216274000">0.06643 BTC</span></span><br></td></tr></tbody></table><div style="padding-bottom:30px;width:100%;text-align:right;clear:both"> <button class="btn btn-success cb"><span data-c="6643000" data-time="1527216274000" data-original-title="" title="">0.06643 BTC</span></button></div></div>
"""

html2 = """
<table class="table table-striped" cellpadding="0" cellspacing="0" style="padding:0px;float:left;margin:0px;width:100%"><tbody><tr><th colspan="3" align="left"><a class="hash-link" href="/tx/a29aa24d2074f2d04a5d917ab33a5cd37e7c2b9d925a9de3de789868f9ff8e72">a29aa24d2074f2d04a5d917ab33a5cd37e7c2b9d925a9de3de789868f9ff8e72</a> <span class="pull-right">2018-05-25 02:45:12</span></th></tr><tr><td class="txtd hidden-phone mobile-f12 stack-mobile"><b>No Inputs (Newly Generated Coins)</b></td><td class="hidden-phone tx-arrow-col"><img src="/Resources/arrow_right_green.png"></td><td class="txtd mobile-f12 stack-mobile"><a href="/address/1C1mCxRukix1KfegAY5zQQJV7samAciZpv">1C1mCxRukix1KfegAY5zQQJV7samAciZpv</a> <span class="pull-right hidden-phone"><span data-c="1261333942" data-time="1527216312000">12.61333942 BTC</span></span><br><font color="red">Unable to decode output address</font> <span class="pull-right hidden-phone"><span data-c="0" data-time="1527216312000">0 BTC</span></span><br></td></tr></tbody></table>
"""

html3 = """
<table class="table table-striped" cellpadding="0" cellspacing="0" style="padding:0px;float:left;margin:0px;width:100%"><tbody><tr><th colspan="3" align="left"><a class="hash-link" href="/tx/9612c4eef497d36cc2955539489e877b3421aabb45fddc468e675900d381362a">9612c4eef497d36cc2955539489e877b3421aabb45fddc468e675900d381362a</a> <span class="pull-right">2018-05-25 02:41:08</span></th></tr><tr><td class="txtd hidden-phone mobile-f12 stack-mobile">bc1q866sv2stppgtywjejsjj3xsfrsm5e2f5zqwsx9z0qcx9k34f0xlqaslnwr<br></td><td class="hidden-phone tx-arrow-col"><img src="/Resources/arrow_right_green.png"></td><td class="txtd mobile-f12 stack-mobile"><a href="/address/33RqHJhbTaLo8Z4UAAphHMiTADrciCxXJf">33RqHJhbTaLo8Z4UAAphHMiTADrciCxXJf</a> <span class="pull-right hidden-phone"><span data-c="1286304026" data-time="1527216068000">12.86304026 BTC</span></span><br>bc1qwqdg6squsna38e46795at95yu9atm8azzmyvckulcc7kytlcckxswvvzej <span class="pull-right hidden-phone"><span data-c="214605974" data-time="1527216068000" data-original-title="" title="">2.14605974 BTC</span></span><br></td></tr></tbody></table>
"""
soup = BeautifulSoup(html3)
#result = soup.find_all('tr')[1].find_all('td')[0].contents[0].string
#result = soup.find_all('tr')[1].find_all('td')[0].contents[0].string
#print(result)
#

a = [1, 2, 3]
for x in a[1:]:
    print(x)
