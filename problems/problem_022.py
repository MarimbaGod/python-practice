# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    list_workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    is_workday = input("What day is it?: ")
    req_gear = []
    if is_workday in list_workdays:
        req_gear.append("laptop")
    else:
        req_gear.append("surfboard")

    list_sunny = ["Sunny", "Totally Radical", "pleasant", "just fine", "Not a cloud in the sky"]
    is_sunny = input("Is it sunny? How's the weather?: ")
    if is_sunny in list_sunny and is_workday not in list_workdays:
        req_gear.append("Your snazzy Ray-Bans")

    if is_sunny in list_sunny and is_workday in list_workdays:
        req_gear.append("workplace appropriate UV-light eye protectors")
    if is_sunny not in list_sunny and is_workday in list_workdays:
        req_gear.append("umbrella")

    if is_sunny not in list_sunny and is_workday not in list_workdays:
        req_gear.append("a wetsuit")
        # req_gear.append()
    print("Okay, you need to bring: ")
    print(req_gear)


gear_for_day("", "")


#can use reg.ex
