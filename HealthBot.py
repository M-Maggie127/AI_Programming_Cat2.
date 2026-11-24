def hospital_bot(user_input):
    text = user_input.lower().strip()
    if text == "hello" or text == "hi":
        return "Hello! How can I help?"
    elif text == "tour maternity" or text == "mama care":
        return "Virtual tour: [link]. Physical tours available everyday from 10am.Includes labor ward, nursery, private rooms. Book free tour?"
    elif text == "emergency mama":
        return "Mama Emergency Protocol:Lie on left side. We are tracking your location. Stay with me mama. Help is coming."
    elif text == "pregnancy" or text == "mama" or text == "delivery":
        return "Mama care at Fremo:" \
        "1)ANTENATAL CLINICS:Mon-Fri 8am-12pm with Dr Meg.Package: 4 visits+scans+labs=18k,NHIF covers 12k." \
        "2)DELIVERY PACKAGES:Normal:85k-2 nights,midwife,padiatrician review;CS:180k-4 nights,theater, NICU standby.NHIF/SHA rebate available. Water birth? Yes." \
        "3)EMERGENCY SIGNS:Come now if:Bleeding,severe headache, no baby movement, waterbreaks." \
        "4)POSTPARTUM:Free check up at 6 wks for mama + baby" \
        "type 'book antenatal' or 'tour maternity' or 'emergency mama'"
    elif user_input.lower() == "insurance":
        return "We accept: NHIF,SHA,AAR,Jubilee,CIC,Madison,Britam;Maternity NHIF rebate 35k."
    elif user_input.lower() == "help":
        return "I can help with:Hours,Insurance,Mama care"
    else:
        return "Sorry I didn't catch that."
def main():
    print("Welcome to the FREMO information Bot! Type 'help' for assistance or 'exit' to 'quit'")
    while True:
        user_input = input ("User: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["exit","bye"]:
            print("HealthBot: Goodbye! Happy to help always!")
            break
        response_text = hospital_bot(user_input)
        print("HealthBot:", response_text)
if __name__ == "__main__":
   main()