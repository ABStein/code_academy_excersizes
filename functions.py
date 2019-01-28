def in_range(num, lower, upper):
  if (num >= lower) and (num <= upper):
    return True
  else: return False


def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif (rating < 9) and (rating >= 6):
    return "This one was fun."
  else: return "Outstanding!"

def divisible_by_ten(num):
	if (num % 10 == 0):
		return True
	else: return False



premium_ground_shipping = 125.00

def ground_shipping(weight):
  if weight <= 2.00:
    return 1.50 * weight + 20 
  elif weight >= 3.00 and weight <= 6.00:
    return 3.00 * weight + 20 
  elif weight >= 7.00 and weight <= 10.00:
    return 4.00 * weight + 20
  elif weight > 10.00:
    return 4.75 * weight + 20
  elif weight >= 22.11:
    return premium_ground_shipping
    
print(ground_shipping(22.11))

def drone_shipping(weight):
  if weight <= 2.00:
    return 4.50 * weight 
  elif weight >= 3.00 and weight <= 6.00:
    return 9.00 * weight
  elif weight >= 7.00 and weight <= 10.00:
    return 12.00 * weight
  elif weight > 10.00:
    return 14.25 * weight
  
print(drone_shipping(3))


def shipping_method(weight):
  if weight <= 3:
    return "You should use Drone Shipping becasue your package will cost " + str(drone_shipping(weight)) + " while Ground Shipping will cost " + str(ground_shipping(weight))
  if weight >= 4 and weight <= 22.10:
    return "You should use Ground Shipping becasue your package will cost " + str(drone_shipping(weight)) + " for Drone Shipping while Ground Shipping will cost " + str(ground_shipping(weight))
  else: return "premium shipping is the way to go"



