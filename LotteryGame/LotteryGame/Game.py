from ast import Delete, Str
import pygame
import random
class TheGame(object):
    def __init__(self,Screen, NumberOfLotteryValues, MaxValue, LowestValue):
        self.done = False
        self.NumberOfLotteryValues = NumberOfLotteryValues
        self.MaxValue = MaxValue
        self.LowestValue = LowestValue
        self.LotteryValues = []
        self.UserInput = ""
        self.DesiredString = ""
        self.Checkrunning = False
        self.WinPersentage = 0
        self.Screen = Screen
        self.Font = pygame.font.Font(None, 24)
        self.ScreenRect = pygame.display.get_surface().get_rect()


        self.Prizes = {
           0: "Nothing",
           17: "10 pounds",
           33: "15 pounds",
           50: "half a million",
           67: "1 Million",
           83: "9 Million",
           100: "1 Billion",
        }
    def Draw(self, surface):
        surface.fill(pygame.Color("black"))

        Discrpition = self.Font.render( "Type out %s Values" % self.NumberOfLotteryValues, True,pygame.Color("white"))
        DiscrpitionRect = Discrpition.get_rect(center=self.ScreenRect.center)
        DiscrpitionRect.y -=40
        surface.blit(Discrpition,DiscrpitionRect)

        PlayerChoises = self.Font.render( self.DesiredString, True,pygame.Color("white"))
        PCRect = PlayerChoises.get_rect(center=self.ScreenRect.center)
        surface.blit(PlayerChoises,PCRect)

        if self.Checkrunning:
            LotteryValues = ""
           
            for LotteryValue in self.LotteryValues:
                LotteryValues = LotteryValues + LotteryValue + " "

            LotteryScore = self.Font.render("The Lottery Values are: "  +LotteryValues, True,pygame.Color("white"))
            LotterScoreRect = LotteryScore.get_rect(center=self.ScreenRect.center)
            LotterScoreRect.y += 40
            surface.blit(LotteryScore,LotterScoreRect)


            PersentageWin = self.Font.render(str(self.WinPersentage)+ "%", True,pygame.Color("white"))
            PersentageWinRect = PersentageWin.get_rect(center=self.ScreenRect.center)
            PersentageWinRect.y += 80
            surface.blit(PersentageWin,PersentageWinRect)

            Prize = self.Font.render(self.Prizes[self.WinPersentage], True,pygame.Color("yellow"))
            PrizeRect = Prize.get_rect(center=self.ScreenRect.center)
            PrizeRect.y += 120
            surface.blit(Prize,PrizeRect)


    def StartGame(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.GetKeyPressed()
            self.Draw(self.Screen)
            pygame.display.update()
            

           
    def GetKeyPressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            self.AddInputKey("0")
        if keys[pygame.K_1]:
            self.AddInputKey("1")
        if keys[pygame.K_2]:
            self.AddInputKey("2")
        if keys[pygame.K_3]:
            self.AddInputKey("3")
        if keys[pygame.K_4]:
            self.AddInputKey("4")
        if keys[pygame.K_5]:
            self.AddInputKey("5")
        if keys[pygame.K_6]:
            self.AddInputKey("6")
        if keys[pygame.K_7]:
            self.AddInputKey("7")
        if keys[pygame.K_8]:
            self.AddInputKey("8")
        if keys[pygame.K_9]:
            self.AddInputKey("9")
        if keys[pygame.K_SPACE]:
            self.AddInputKey("0")
        if keys[pygame.K_RETURN]:
            if len(self.UserInput) <  self.NumberOfLotteryValues*3-1:
                self.RunCheck()
        if keys[pygame.K_DELETE]:
            self.UserInput = []
            self.DesiredString = []
        if keys[pygame.K_BACKSPACE]:
            self.BackSpacePessed()


    def AddInputKey(self,Key):
        if self.Checkrunning:
            return
        if len(self.UserInput) <  self.NumberOfLotteryValues*3-1:
            self.DesiredString = self.DesiredString.replace(" _","")
            self.DesiredString = self.DesiredString.replace("_","")

            self.UserInput = self.UserInput + Key

            if len(self.UserInput) % 3 == 2:
                self.DesiredString = self.DesiredString + Key + " _"
                self.UserInput = self.UserInput + ","
            else:
                if Key == "0":
                    self.DesiredString = self.DesiredString + "  _"
                elif int(Key) > 4:
                    if int(Key) == 5:
                        self.UserInput = self.UserInput + "0,"
                        self.DesiredString = self.DesiredString + " %s0 _" %  Key 
                        print(self.DesiredString)
                        return
                    else:
                        self.UserInput = self.UserInput[:-1]
                        self.UserInput = self.UserInput + "0%s," %  Key 
                        self.DesiredString = self.DesiredString + " %s _" %  Key 
                else:
                    self.DesiredString = self.DesiredString + " %s_" %  Key 
                    
            
            print(self.DesiredString)
        else:
            self.RunCheck()
    def BackSpacePessed(self):
        if self.Checkrunning:
            return
        if len(self.UserInput) > 0:
            if len(self.UserInput) % 3 != 2:
                if len(self.UserInput) % 3 == 1:
                    self.DesiredString =  self.DesiredString[:-2]
                    self.DesiredString = self.DesiredString+ "_"
                   
                else:
                    
                    if self.UserInput[-2] != "0" and self.UserInput[-3] == "0":
                        self.DesiredString =  self.DesiredString[:-3]
                        self.UserInput = self.UserInput[:-2]
                        self.DesiredString = self.DesiredString+ "_"

                    else:
                        self.DesiredString =  self.DesiredString[:-4]
                        self.UserInput = self.UserInput[:-2]
                        self.DesiredString = self.DesiredString+ "_"
                   
            self.UserInput = self.UserInput[:-1]
        print(self.DesiredString)

    def RunCheck(self):
        self.Checkrunning = True

        for i in range(1, self.NumberOfLotteryValues+1):
            self.LotteryValues.append( str(random.randrange( self.LowestValue, self.MaxValue)))

        self.UserInput = self.UserInput[:-1]
        UserLotteryValues = [int(Values) for Values in self.UserInput.split(",")]
      
        print (UserLotteryValues)

        for i in range(0, self.NumberOfLotteryValues):
            if(self.LotteryValues[i] == str(UserLotteryValues[i]) ):
                self.WinPersentage += 100/self.NumberOfLotteryValues
                print(self.LotteryValues[i] + " is equal to  " +str(UserLotteryValues[i])  )
            else:
                print(self.LotteryValues[i] + " not equal to  " +str(UserLotteryValues[i])  )
        
        self.WinPersentage = round(self.WinPersentage)   
        print(str(self.WinPersentage) + " is the win persentage")
        self.LotteryValues