# Flos Economy Simulator - Version 0.1

village = "Woodmere"
gold = 500
grain = 100
milk = 60

print("=== FLOS ECONOMY SIMULATOR ===")
print("Village:", village)
print("Gold:", gold)
print("Grain:", grain)
print("Milk:", milk)

trading_settlements = ["Oakshade", "Thornbrook", "Forestbrook", "Brightstone"]

print("Pick your destination")
print("1", trading_settlements[0])
print("2", trading_settlements[1])
print("3", trading_settlements[2])
print("4", trading_settlements[3])

destination = int(input("Enter a number (1-4): "))

grain_prices = {
  trading_settlements[0]:5,
  trading_settlements[1]:3,
  trading_settlements[2]:6,
  trading_settlements[3]:7
}

milk_prices ={
  trading_settlements[0]:3,
  trading_settlements[1]:2,
  trading_settlements[2]:2,
  trading_settlements[3]:4}

if 1 <= destination <= 4:
  
  destination_settlement = trading_settlements[destination - 1]
  
  print("You are traveling to:", destination_settlement)
  print("Grain prices are:", grain_prices[destination_settlement])
  print("Milk prices are:", milk_prices[destination_settlement])

  print("What would you like to sell?")
  print("1. Grain")
  print("2. Milk")

  product_to_sell = int(input("Pick a product(1-2):"))
  
  if product_to_sell == 1 :
  
   grain_to_sell = int(input("How much grain do you want to sell? "))

   if 0 < grain_to_sell <= grain:
    gold_earned = grain_to_sell*grain_prices[destination_settlement]
    gold += gold_earned
    grain -= grain_to_sell
    print("Trade successful!")
    print("Gold earned:", gold_earned)
    print("Total gold:", gold)
    print("Remaining grain:", grain)

   else:
    print("Invalid quantity!")

  elif product_to_sell == 2 :
    milk_to_sell = int(input("How much milk do you want to sell? "))
    if 0 < milk_to_sell <= milk:
     gold_earned = milk_to_sell*milk_prices[destination_settlement]
     gold += gold_earned
     milk -= milk_to_sell
     print("Trade successful!")
     print("Gold earned:", gold_earned)
     print("Total gold:", gold)
     print("Remaining milk:", milk)

    else:
     print("Invalid quantity!")

  else:
    print("Invalid product selection!")


else:

  print("Invalid destination! , Please select a valid choice (1-4)")
