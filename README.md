# Web_scraping_memeimageWebsite_imgflip_PYTHON_ipynb
get all images from imgflip.com

[ ]
import requests
import shutil
import time
from bs4 import BeautifulSoup
import json
import os
import csv
filecsv = open('meme.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://imgflip.com/?page='
try:
  os.mkdir("images")
except FileExistsError:
  shutil.rmtree("/content/images")
  os.makedirs("images")
file = open('meme.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['author', 'title', 'img']
writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
writer.writeheader()

for page in range(1,11):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all('div', {'class': "base-unit clearfix"})
    i = 0
    for pt in ancher:
        try:
          img = pt.find('img', {'class': 'base-img'})['src']
        except TypeError:
          try:
            img = pt.find('video', {'class': 'base-img ctx-gif'})['data-src']
          except TypeError:
            img="img not availabe"
        try:
          title = pt.find('h2', {'class': 'base-unit-title'}).find('a').get_text()
        except AttributeError:
          title='not availabe'
        try:
          author = pt.find('a', {'class': 'u-username'}).get_text()
        except AttributeError:
          author='not availabe'

        if img !="img not availabe":
          resource = requests.get("http:"+img)
          # print("status_code",resource.status_code)
          if (img.endswith(".jpg")):
            output = open("images/"+title.replace('/',"")+str(page)+author+".jpg","wb")
          else:
            output = open("images/"+title.replace('/',"")+str(page)+author+".gif","wb")
          output.write(resource.content)
                
          output.close()
        else: print("img not availabe")
        print("image: "+"https:"+img)
        print("title: ",title)
        print("author: ", author)

        writer.writerow({'author': author.strip('\r\n'), "title":title,"img":img})

        data['img'] = img
        data['title'] = title
        data['author'] = author
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")
file.write("\n]")
# defining the api-endpoint
filecsv.close()
file.close()

print(len(os.listdir('/content/images')), "images are extracted")

--- 1 ---
https://imgflip.com/?page=1
image: https://i.imgflip.com/70wn2t.jpg
title:  I still can’t, too much chlorine
author:  Iceu.
image: https://i.imgflip.com/70wnrs.jpg
title:  It’s so annoying
author:  Iceu.
image: https://i.imgflip.com/70rnq7.jpg
title:  I’m not wrong technically
author:  Iceu.
image: https://i.imgflip.com/70ra61.gif
title:  trust me it works
author:  F_AlphabetLore
image: https://i.imgflip.com/70n25b.jpg
title:  *dies of death*
author:  Iceu.
image: https://i.imgflip.com/70rn65.jpg
title:  True story tbh
author:  Iceu.
image: https://i.imgflip.com/711q5g.jpg
title:  Too true
author:  Iceu.
image: https://i.imgflip.com/70ywr4.gif
title:  How teachers expect us to Leave the the Building during a Fire Drilll
author:  JustaCheemsDoge
image: https://i.imgflip.com/70tdf7.jpg
title:  Empty Stonks
author:  YellowBlack
image: https://i.imgflip.com/70zi9p.jpg
title:  creative title
author:  MBomb
image: https://i.imgflip.com/70o41c.gif
title:  title
author:  YellowBlack
image: https://i.imgflip.com/70n1kx.gif
title:  Here’s the Plague Doctor video I promised all of you! It’s not the best but LeDank and I were in a rush; was starting to rain
author:  Iceu.
image: https://i.imgflip.com/70u3d8.jpg
title:  Clever Title
author:  Sauce.
image: https://i.imgflip.com/70qkhq.jpg
title:  So messy ... but so good!
author:  who_am_i
--- 2 ---
https://imgflip.com/?page=2
image: https://i.imgflip.com/70p85j.gif
title:  Clever title
author:  Sauce.
image: https://i.imgflip.com/710min.jpg
title:  See?
author:  Turkey_LeDank
image: https://i.imgflip.com/70nmw9.jpg
title:  The School System
author:  Kevvin101
image: https://i.imgflip.com/5xvadx.jpg
title:  Panik Kalm Panik
author:  TheRandomania_CO
image: https://i.imgflip.com/70qsme.jpg
title:  thanks, google.
author:  Thankful-LucotIC
image: https://i.imgflip.com/70y426.gif
title:  they're after me
author:  Eat_dry_cereal
image: https://i.imgflip.com/70jjm3.jpg
title:  It keeps short circuiting, someone help :(
author:  Iceu.
image: https://i.imgflip.com/711rbl.jpg
title:  Relatable :)
author:  Iceu.
image: https://i.imgflip.com/70qmq4.gif
title:  You're at school recess and...
author:  8Viso
image: https://i.imgflip.com/70np8r.jpg
title:  School lunch be like
author:  Dreamykid42
image: https://i.imgflip.com/70ws7t.jpg
title:  I am smort
author:  10001008
image: https://i.imgflip.com/70yxhc.gif
title:  real
author:  ClayCrabz_Alt
image: https://i.imgflip.com/70r40y.jpg
title:  Guy Holding Cardboard Sign
author:  cooliojulio12
image: https://i.imgflip.com/70yyk2.jpg
title:  modern solutions require modern problems
author:  quacksaysduck
--- 3 ---
https://imgflip.com/?page=3
image: https://i.imgflip.com/70uguc.jpg
title:  elmo cocaine
author:  jman234567
image: https://i.imgflip.com/70v13u.jpg
title:  *world breaks*
author:  potassiumking
image: https://i.imgflip.com/70ppny.jpg
title:  I’m back
author:  TheMemeDebunker
image: https://i.imgflip.com/70xu2a.jpg
title:  It's kinda true tho
author:  Manimal14
image: https://i.imgflip.com/70nxgf.jpg
title:  girls getting 95% on the exam vs. boys getting 70% on the exam
author:  NiChrosian
image: https://i.imgflip.com/70hgun.gif
title:  so true
author:  YellowBlack
image: https://i.imgflip.com/70n6pe.jpg
title:  oh slap funny
author:  Fastbear6798
image: https://i.imgflip.com/70v2g3.jpg
title:  I Bet He's Thinking About Other Women
author:  Mettaton00101
image: https://i.imgflip.com/70n3u4.jpg
title:  *screaming intensifies*
author:  taco_mel
image: https://i.imgflip.com/70wj7f.jpg
title:  not availabe
author:  Kilo_07
image: https://i.imgflip.com/70p5sl.jpg
title:  Ok
author:  MK8DX_Country
image: https://i.imgflip.com/70xrvd.jpg
title:  hmmmm...
author:  Spooky_TotallyNotTez
image: https://i.imgflip.com/70hgnz.gif
title:  so true
author:  YellowBlack
image: https://i.imgflip.com/70r1m0.jpg
title:  pls enlist
author:  ytpmemer_2022
--- 4 ---
https://imgflip.com/?page=4
image: https://i.imgflip.com/70g38c.gif
title:  Angery
author:  Iceu.
image: https://i.imgflip.com/70v1n8.jpg
title:  Who the heck even does this!?!?
author:  AA69
image: https://i.imgflip.com/70pdv7.jpg
title:  du tu tu du du du du bum du du dum (Anyone else?)
author:  Thatdumbshityeetman
image: https://i.imgflip.com/70r7ur.jpg
title:  Bad Pun Dog
author:  TheFakeAbigblueworld
image: https://i.imgflip.com/70w6o9.jpg
title:  Babys be like
author:  I_Love_Games_YT
image: https://i.imgflip.com/70v48b.jpg
title:  Sorry it offended you, its just a joke
author:  Thiccmemegod33
image: https://i.imgflip.com/70u1am.jpg
title:  I See Stupid People
author:  VinceVance
image: https://i.imgflip.com/70jk3k.jpg
title:  2nd one is me
author:  Iceu.
image: https://i.imgflip.com/70jw7w.gif
title:  opaegtub;bg
author:  BLURRY-NUGGET-HOT-SAUCE-IS-BACK
image: https://i.imgflip.com/70pph4.jpg
title:  Relatable, right?
author:  gforce810
image: https://i.imgflip.com/70ohpi.jpg
title:  HE DID IT
author:  mareeep
image: https://i.imgflip.com/70l7zu.jpg
title:  hol up...
author:  kaneishere123
image: https://i.imgflip.com/70wbcv.jpg
title:  ummm
author:  Meme_Making_Machine
image: https://i.imgflip.com/70wqp8.gif
title:  My food DID taste a little "mild"...
author:  X-mas-energeticbombhands
--- 5 ---
https://imgflip.com/?page=5
image: https://i.imgflip.com/70rbmb.jpg
title:  who else hate's racism?
author:  ultimatebaddie69_420
image: https://i.imgflip.com/70v29o.jpg
title:  This Is Where I'd Put My Trophy If I Had One
author:  SQUISHIE
image: https://i.imgflip.com/70xvao.gif
title:  School
author:  LCBolt
image: https://i.imgflip.com/70mnax.jpg
title:  i have very strong opinions on this
author:  WiltingRose
image: https://i.imgflip.com/70ao07.gif
title:  True tho
author:  MrCheezit
image: https://i.imgflip.com/6scf1t.jpg
title:  Am I wrong??
author:  ImStillOnSmoko024
image: https://i.imgflip.com/70xizp.gif
title:  how to train your puppy
author:  EssoHegazy
image: https://i.imgflip.com/70tjex.jpg
title:  I Bet He's Thinking About Other Women
author:  Luka_an_gamer
image: https://i.imgflip.com/70mybt.jpg
title:  Pain
author:  Player64
image: https://i.imgflip.com/70l896.jpg
title:  I don’t like using imgflip on my phone
author:  CypressTree
image: https://i.imgflip.com/70racs.jpg
title:  I've won but at what cost?
author:  meme_lord_38
image: https://i.imgflip.com/706dol.jpg
title:  Free money!
author:  Iceu.
image: https://i.imgflip.com/70p4j6.jpg
title:  …
author:  DejaView
image: https://i.imgflip.com/70jvln.jpg
title:  Doggo
author:  Anog
--- 6 ---
https://imgflip.com/?page=6
image: https://i.imgflip.com/70uw4f.jpg
title:  Spirit Halloween
author:  DanksoftheMeme
image: https://i.imgflip.com/70ic7x.gif
title:  Am I wrong?
author:  Doodle.Of.Chaos
image: https://i.imgflip.com/70bwyv.gif
title:  title
author:  YellowBlack
image: https://i.imgflip.com/70nu6p.jpg
title:  Trade Offer
author:  chickentendeys
image: https://i.imgflip.com/70qqmk.gif
title:  This is probably so relatable -_-
author:  Ineedtotouchgrass
image: https://i.imgflip.com/6zway6.gif
title:  Why is it like that though
author:  Iceu.
image: https://i.imgflip.com/70s6su.jpg
title:  Tom chasing Harry and Ron Weasly
author:  g_user_109928068361566909048
image: https://i.imgflip.com/70qjs8.jpg
title:  When a meme becomes self aware
author:  who_am_i
image: https://i.imgflip.com/70u96x.jpg
title:  Champagne before Christmas please
author:  Lamejokey
image: https://i.imgflip.com/70qeu1.jpg
title:  Original Title
author:  OliverHutchinson1
image: https://i.imgflip.com/70r1qs.gif
title:  mmmmmmmmmmmmmmmmmmmmmmmm
author:  shrne
image: https://i.imgflip.com/70ukwc.jpg
title:  That Makes No Sense
author:  LadyDeerHeart
image: https://i.imgflip.com/70qlq1.gif
title:  Tests
author:  ______________HI
image: https://i.imgflip.com/70ntdn.jpg
title:  Cube
author:  CornSyrup
--- 7 ---
https://imgflip.com/?page=7
image: https://i.imgflip.com/70g3us.jpg
title:  Who actually watches the whole thing
author:  Iceu.
image: https://i.imgflip.com/70bg0t.jpg
title:  I will become the robber
author:  Iceu.
image: https://i.imgflip.com/70jv2j.jpg
title:  not availabe
author:  KitCat5416
image: https://i.imgflip.com/70u8nx.jpg
title:  This is actually real (IMDb link in comments)!
author:  Redneck64xD
image: https://i.imgflip.com/70huvz.gif
title:  Your dad
author:  DamnthatsFunny_93
image: https://i.imgflip.com/70jv73.jpg
title:  Rolex
author:  propeacenow
image: https://i.imgflip.com/70e3io.jpg
title:  terrible memes
author:  fixtechstuff
image: https://i.imgflip.com/70xcsw.gif
title:  Are you Ready
author:  GamerM16
image: https://i.imgflip.com/7110mz.jpg
title:  Huh Dog
author:  idk.jpg
image: https://i.imgflip.com/70jw2m.jpg
title:  Comment rocket launcher memes LOL
author:  Enderboi09
image: https://i.imgflip.com/70bgfz.jpg
title:  This is pain
author:  Iceu.
image: https://i.imgflip.com/70ueb3.jpg
title:  the more you know
author:  thelastcumbender
image: https://i.imgflip.com/70z1a4.jpg
title:  free Smen
author:  maplemaker101
image: https://i.imgflip.com/70k93h.jpg
title:  Just Run
author:  Limeon55
--- 8 ---
https://imgflip.com/?page=8
image: https://i.imgflip.com/70xb1b.jpg
title:  The one on the left is actually green
author:  TriangleHead
image: https://i.imgflip.com/70ju70.jpg
title:  Sonic Boom Knuckles gives you life advice
author:  LEGO_Clayface
image: https://i.imgflip.com/7019bo.jpg
title:  I am evil >:)
author:  Iceu.
image: https://i.imgflip.com/70yvqi.jpg
title:  damn that sucks
author:  ClayCrabz_Alt
image: https://i.imgflip.com/70wbsj.jpg
title:  Literately everyone looking at this
author:  Calebisbetterer
image: https://i.imgflip.com/70ytjt.jpg
title:  every type of creator has their own dream
author:  ThisRandomJake
image: https://i.imgflip.com/706egb.gif
title:  True ngl
author:  Iceu.
image: https://i.imgflip.com/6zvc8b.jpg
title:  rip the kid
author:  Qtz
image: https://i.imgflip.com/70rb7v.jpg
title:  WOOHOO!
author:  MopMan
image: https://i.imgflip.com/70x59h.gif
title:  The strange bridge
author:  Tifflamemez_Turkey_Drip
image: https://i.imgflip.com/70xdo6.jpg
title:  nostalgia
author:  YellowBlack
image: https://i.imgflip.com/70w2t7.jpg
title:  you're the last one, complete the mission
author:  2182929
image: https://i.imgflip.com/70jj6p.gif
title:  Why?
author:  Lil_Ginge08
image: https://i.imgflip.com/70repw.jpg
title:  Time Machine Failure
author:  Lamejokey
--- 9 ---
https://imgflip.com/?page=9
image: https://i.imgflip.com/70rspm.jpg
title:  This is sad
author:  Sir_Eman
image: https://i.imgflip.com/70n5lh.jpg
title:  Tuxedo Winnie The Pooh
author:  imakegoodmemes.com
image: https://i.imgflip.com/70ytfc.jpg
title:  Cheating
author:  WayneUrso
image: https://i.imgflip.com/70xpln.jpg
title:  I'm The Captain Now
author:  Sanic_thehotdog153
image: https://i.imgflip.com/7018wt.jpg
title:  I wish he worked for me lol
author:  Iceu.
image: https://i.imgflip.com/6zzs4l.gif
title:  WTF BTS AGAIN!??
author:  SIKE_itzmeZ
image: https://i.imgflip.com/70jy13.gif
title:  Arrested after leaving the purse in bathroom
author:  Tifflamemez_Turkey_Drip
image: https://i.imgflip.com/70k72n.jpg
title:  Hehe i just broke a bone..
author:  TessaStarzYT
image: https://i.imgflip.com/70z237.jpg
title:  you know what this means after opening the chips...
author:  icyteams
image: https://i.imgflip.com/70r00d.jpg
title:  Bruh.
author:  memeboi12E
image: https://i.imgflip.com/6zhid0.jpg
title:  Shades Design is literal perfection
author:  one_gud_guy
image: https://i.imgflip.com/6znm2e.jpg
title:  C o o k i e s
author:  Iceu.
image: https://i.imgflip.com/70ztpr.jpg
title:  i will
author:  GyroZeppli
image: https://i.imgflip.com/70lagb.jpg
title:  Did anyone else think this was torture?
author:  ItsKyFa1
--- 10 ---
https://imgflip.com/?page=10
image: https://i.imgflip.com/6zrllt.gif
title:  I’m not wrong though
author:  Iceu.
image: https://i.imgflip.com/70vuur.gif
title:  Snakes
author:  Tifflamemez_Turkey_Drip
image: https://i.imgflip.com/70wk9c.jpg
title:  Only in ohio
author:  SaiVijay1
image: https://i.imgflip.com/70bii5.gif
title:  title
author:  Kid-Named-LAKS
image: https://i.imgflip.com/70za13.jpg
title:  Dad Joke Dog
author:  Axton2k8
image: https://i.imgflip.com/70jxgd.gif
title:  That never happens
author:  techboy30
image: https://i.imgflip.com/710w2p.jpg
title:  Wow, I want to know where she ate.
author:  who_am_i
image: https://i.imgflip.com/70rydg.jpg
title:  its true tho
author:  StackOPancakes
image: https://i.imgflip.com/70v2fr.jpg
title:  Mad skeleton
author:  Your_local_wienerdog
image: https://i.imgflip.com/70lah8.jpg
title:  two buttons 1 blue
author:  Memin-Sanchez
image: https://i.imgflip.com/710czy.jpg
title:  PIKACHU NO
author:  XxSimmyxX
image: https://i.imgflip.com/70tf5h.jpg
title:  Based
author:  PEVvalentin
image: https://i.imgflip.com/70zl9f.jpg
title:  {title}
author:  -Crystaleon_28-
image: https://i.imgflip.com/70zkbp.jpg
title:  UNO Draw 25 Cards
author:  KHLOELUCK
139 images are extracted
