def greater_than(x, y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y:
    return "These numbers are the same"
    
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
  
print(graduation_reqs(120))


def applicant_selector(gpa, ps_score, ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
    return "This applicant should be given an in-person interview."
  else: return "This applicant should be rejected."