str="""lockdown may be imminent in Maharashtra, but the word itself may be avoided to cause panic, sources told CNN-News18 after Chief Minister Uddhav Thackeray’s crucial meeting with the state’s Covid task force amid an exponential rise in virus cases and deaths.
A detailed discussion on medical facilities, and management of hospitals amid the crisis was carried out, the sources said. As cases spiral in Maharashtra, its healthcare services have been stretched and various hospitals have reported shortage of medical necessities such as oxygen, or ventilators.
Covid-19, which acts as a deadly respiratory disease in its most serious cases, often causes a patient’s oxygen levels to drop, making the supply a necessity in said cases.
The improvement of medical facilities and optimum use of available medical infrastructure were discussed in great detail, the sources added. Coordination at a Centre-state level to control the surging infections, was also discussed by the officials."""
count=0
word_list=str.split()
for word in word_list:
    count=count+1
print(count)
