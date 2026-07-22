name = input("enter your real name, Club member:  ")
club = input("enter your school club name: ")


member_number = 8
points_earned = 9.5
event_count = 6
meeting_hours = 1.5
is_active = True


print("Name,", name, "-> type:", type(name))
print("Club:", club, "-> type:", type(name))
print("member number:", member_number, "-> type:", type(member_number))
type(member_number)
print("Points Earned:", points_earned, "-> type:",type(points_earned))
type(points_earned)
print("Event Count:", event_count, "-> type:",type(event_count))
print("Meeting hours:", meeting_hours, "-> type:", type(meeting_hours))
print("Is Active:", is_active, "-> type:",type(is_active)) 
member_number_text =str(member_number)  
event_count_text =str(event_count)  
points_text = str(points_earned) 
status_text = str(is_active)                                         

print("Member Numberas text:", points_text, "-> type:",type(points_text))
print("Event Count as Text:", points_text, "-> type:",type(event_count_text))
print("points as text:", status_text,"->type:",type(points_text))
print("status as text:", status_text, "->type:",type(status_text))

first_three = name,{0:3}
last_letter = name,{-1:}
badge_code = first_three + last_letter

print("first 3 letters of name:", last_letter)
print("last letter of name:", last_letter)
print("badge code:", badge_code)

print("first 3 letters of name:", first_three)
print("last letter of name:", last_letter)
print("badge code:", badge_code)

reversed_club = club:{::-1}
print("reversed club name:", reversed_club)

badge_line_1 = "CLUB MEMBER " + badge_code.upper()
badge_line_2 = "ID: " + member_number_text + " | EVENTS:" + event_count_text
badge_line_3 = "POINTS: " + points_text + " | EVENTS:" + status_text
badge_line_4 = "SECRET CLUB CODE: " + reversed_club.upper()

print("")
print("===== SCHOOL CLUB MEMBER BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===========================")