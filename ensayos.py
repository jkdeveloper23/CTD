#Lol surrender emulator beta 25wt4f5
surrender = []
yes= 0

no= surrender.count(0)

for v in surrender:
	yes= yes+v

if no < 2 and yes >= 3:
	print("Surrender with {} yes and {} no ".format(yes, no))
else:
	print("continue playing")

print("Yes= {} and no= {}".format(yes,no))