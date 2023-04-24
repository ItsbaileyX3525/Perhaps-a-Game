from ursina import *


app=Ursina(vsync=60)
window.borderless=False
window.exit_button.visible=False
window.fps_counter.visible=False
################
# Clicker game!#
################
application.assets_folder='assets/'
multiplier=1
ClickerDudeClicks=0
ClickerDudeAutoClicks=0
ClickerDudeAutoClicksCost=50
ClickerDudeClicksMultiplier=1
ClickerDudeClicksMultiplierCost=25
ClickerDudeShovels=0
ClickerDudeDonuts=0
ClickerDudesSingle=0
CurrentPage=1

def ClickerDudeUpdate():
    global ClickerDudeClicks
    ClickerDudeClicks+=1*ClickerDudeClicksMultiplier*multiplier
    MainClickerDude.scale = [e*1.25 for e in [.1,.1]]
    MainClickerDude.animate('scale_x', .15, duration=.1)
    MainClickerDude.animate('scale_y', .15, duration=.1)

def ClickerDudeAutoCollectorBuy1Func():
    global ClickerDudeClicks,ClickerDudeAutoClicks,ClickerDudeAutoClicksCost
    if ClickerDudeClicks>=ClickerDudeAutoClicksCost:
        if ClickerDudeAutoClicks==0:
            ClickerDudeAutoCollectorBuy1GenerateFunc()
        ClickerDudeClicks -= ClickerDudeAutoClicksCost
        ClickerDudeAutoClicks+=1
        ClickerDudeAutoClicksCost += 12

def ClickerDudeAutoCollectorBuy1GenerateFunc():
    global ClickerDudeClicks
    ClickerDudeClicks += 1 * ClickerDudeAutoClicks
    s = Sequence(Wait(1),Func(ClickerDudeAutoCollectorBuy1GenerateFunc))
    s.start()

def ClickerDudeClicksMultiplierFunc():
    global ClickerDudeClicksMultiplier, ClickerDudeClicksMultiplierCost,ClickerDudeClicks
    if ClickerDudeClicks >= ClickerDudeClicksMultiplierCost:
        ClickerDudeClicks -= ClickerDudeClicksMultiplierCost
        ClickerDudeClicksMultiplierCost += 35
        ClickerDudeClicksMultiplier += 1

def ClickerDudeCookieShop():
    global CurrentPage
    if CurrentPage==1:
        pass
    elif CurrentPage==2:
        ClickerDudeAutoCollectorBuy1.enabled=True
        ClickerDudeUpgrade.enabled=True
        CurrentPage=1

        

ClickerDudeAutoCollectorBuy1=Button(scale_x=.125,scale_y=.135,x=-.3,y=-.22,icon='click.png',color=color.clear,on_click = ClickerDudeAutoCollectorBuy1Func)
ClickerDudeAutoCollectorBuy1Text=Text(text=f'Buy to earn 1 <gold>cookie \n<white>every second!\n\nCost: {ClickerDudeAutoClicksCost}',x=-.2,y=-.2)
ClickerDudeUpgrade=Button(scale_x=.125,scale_y=.125,icon='CookieUpgrade.png',color=color.clear,x=.2,y=-.22,on_click=ClickerDudeClicksMultiplierFunc)
ClickerDudeUpgradeText=Text(text=f'Upgrade <purple>clicks!\n\n<white>Cost: {ClickerDudeClicksMultiplierCost}',x=.3,y=-.2)

def ClickerDudeShovelShop():
    pass

def ClickerDudeDonutShop():
    pass

def ClickerDudeSingleShop():
    pass

MainClickerDude=Button(icon='cookie.png',scale=.15,y=.1,x=.1,on_click=ClickerDudeUpdate,color=color.clear)
ClickerDudeText=Text("Cookies: 0",y=.4,x=.05)
ClickerDudeShopMenuBar=Entity(model='quad',color=color.gray,scale_x=20,scale_y=4,y=-3.2)
def ClickerDudeUpdateLoop():
    ClickerDudeText.text=f"Cookies: {ClickerDudeClicks}"
    ClickerDudeAutoCollectorBuy1Text.text=f'Buy to earn 1 <gold>cookie \n<white>every second!\n\nCost: {ClickerDudeAutoClicksCost}'
    ClickerDudeUpgradeText.text=f'Upgrade <purple>clicks!\n\n<white>Cost: {ClickerDudeClicksMultiplierCost}'
    ClickerDudeText.create_background()
    if ClickerDudeClicks>=100000 and ClickerDudeShovels>=10000 and ClickerDudeDonuts>=1000 and ClickerDudesSingle>=100:
        Begin()
ClikcerDudeUpdateUpdater=Entity(update=ClickerDudeUpdateLoop)

ClickerDudeAutoCollectorIcon=Button(icon='cookie.png',scale=.15,y=-.25,x=-.8,color=color.clear,on_click=ClickerDudeCookieShop)
ClickerDudeAutoCollectorIcon2=Button(icon='donut.png',scale=.15,y=-.425,x=-.8,color=color.clear,on_click=ClickerDudeDonutShop)
ClickerDudeAutoCollectorIcon3=Button(icon='shovel.png',scale=.15,y=-.25,x=-.64,color=color.clear,on_click=ClickerDudeShovelShop)
ClickerDudeAutoCollectorIcon4=Button(icon='single.png',scale=.15,y=-.425,x=-.64,color=color.clear,on_click=ClickerDudeSingleShop)
ClickerDudeAutoCollectorIconBarrier=Entity(model='quad',scale_y=5,scale_x=.5,y=-3.63,x=-4,color=color.black,z=-1)

def Begin():
    pass


app.run()