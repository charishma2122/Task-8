'''Part A
Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume.
Specify brand in a constructor parameter.
Channel should be 1 by default. Volume should be 50 by default.'''
class TV:
    def __init__(self, brand):
        self.brand = brand #created an instance of the TV class
        self.channel = 1 # Default channel will 1
        self.price = 0  # Set default price to 0
        self.inches = 0  # Set default inches to 0
        self.on = False  # TV is initially off
        self.volume = 50  # Default volume set to 50
    ''' Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.'''
    def increase_volume(self): # method1 was to increase the volume of the tv
        if self.volume < 100: # Maximum volume of the TV was 100
            self.volume += 1 # Checking the if the volume should be always 100, if the above condition satisfys the loop will be iterated
            print(f"Volume increased to {self.volume}") # When the volume was assigned , the value will be displayed
        else:
            print("Maximum volume reached") # If volume was assigned to above 100 we will display maxium volume has be reached
    def decrease_volume(self): # # method2 was to decrease the volume of the tv
        if self.volume > 0: # checking if the current volume (self.volume) is greater than 0
            self.volume -= 1 # when the above condition is true , the voulume will be decreased by 1 unit
            print(f"Volume decreased to {self.volume}") # After decrementing the volume, this line prints a message the new volume level
        else:
            print("Minimum volume reached") # where the volume cannot be decreased anymore , displaying an output that minimum we reached
        '''Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel.'''
    def set_channel(self, channel_number): # This method takes the channel_number as a parameter
        if 1 <= channel_number <= 50: # If the channel_number is within the valid range
            self.channel = channel_number #  If the channel_number is within the valid range,
            print(f" channel change to:  {self.channel}") # It prints a message confirming the successful change to the specified channel
        else:
            print("channel not found ")
    def reset_tv(self): #This method returns information about the TV's status.
        self.channel = 1
        self.volume = 50
        print("TV reset to default settings")
    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

class LEDTV(TV): # # LEDTV inherits the TV class
    def __init__(self, brand): # This is the initialization method for the LEDTV class.
        super().__init__(brand) #  initialize attributes inherited from the base class and then initializes additional attributes specific to an LED TV
        self.screen_thickness = None # Initializes the attribute screen_thickness for an LED TV.
        self.energy_usage = None #Initializes the attribute energy_usage for an LED TV
        self.lifespan = None # Initializes the attribute lifespan for an LED TV
        self.refresh_rate = None # Initializes the attribute refresh_rate for an LED TV
        self.viewing_angle = None # Initializes the attribute viewing_angle for an LED TV
        self.backlight = None #Initializes the attribute backlight for an LED TV

    def display_details(self): #
        return f"Brand: {self.brand}\nScreen Thickness: {self.screen_thickness}\nEnergy Usage: {self.energy_usage}\nLifespan: {self.lifespan}\nRefresh Rate: {self.refresh_rate}\nViewing Angle: {self.viewing_angle}\nBacklight: {self.backlight}"

class PlasmaTV(TV):
    def __init__(self, brand):
        super().__init__(brand)
        self.screen_thickness = None
        self.energy_usage = None
        self.lifespan = None
        self.refresh_rate = None
        self.viewing_angle = None
        self.backlight = None

    def display_details(self):
        return f"Brand: {self.brand}\nScreen Thickness: {self.screen_thickness}\nEnergy Usage: {self.energy_usage}\nLifespan: {self.lifespan}\nRefresh Rate: {self.refresh_rate}\nViewing Angle: {self.viewing_angle}\nBacklight: {self.backlight}"

# assigning the parameters to pass
led_tv = LEDTV("Sony")
led_tv.channel = 8
led_tv.volume = 50
print(led_tv.status())  # Sony at channel 8, volume 50

led_tv.inches = 45
led_tv.price = 2000
led_tv.screen_thickness = "Thin"
led_tv.energy_usage = "Moderate"
led_tv.lifespan = "5-20 years"
led_tv.refresh_rate = "150"
led_tv.viewing_angle = "160 degrees"
led_tv.backlight = "LED"

print(led_tv.display_details())
