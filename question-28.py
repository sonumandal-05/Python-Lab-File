# Q8. A person goes to the US Embassy to apply for a tourist visa. The embassy management
# grants a visa if it fulfils the following three conditions:
# He has negative RT-PCR report. Or
# He is fully vaccinated. and His duration of tour is greater than 1 and not more than 15 days.



rt_pcr_report = input("Do you have a negative RT-PCR report? (yes/no): ").strip().lower()
fully_vaccinated = input("Are you fully vaccinated? (yes/no): ").strip().lower()
duration_of_tour = int(input("Enter the duration of your tour in days: "))
if (rt_pcr_report == "yes") or (fully_vaccinated == "yes" and 1 < duration_of_tour <= 15):
    print("Congratulations! Your visa has been granted.")
else:
    print("Sorry, your visa application has been denied.")
    
