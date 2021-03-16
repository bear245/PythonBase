import Calys
import Menu


# def cls():
#    os.system('cls' if os.name=='nt' else 'clear')





Calys.Init()

# Menu.Calys_Menu()
# Calys.Send_Request('MEAS:VOLT? 10V, 5')
Calys.Measurement(Unit='VOLT', Range='10V', Average=2, Iter=3)


Calys.Stop()
# Units = (Calys_Set_Range(Function='VOLT', VRange=20))
# Calys_Calibration(Start_Cal=0, Stop_Cal=20, Step_Cal=5, End_of_String=Units)



# time.sleep(5.5) # Pause 5.5 seconds
# wait = input('Press any key to continue...')
# TODO 1) Develop a function for Voltage Measurement use Calys_Calibration as example
#      2) Implement Voltage measurement into Main_Menu
