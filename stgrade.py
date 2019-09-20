
st_list=[];
totalscore=300
inp=int(input("Total number of student:"))
def st_record():
    for index in range(0,inp):
        name=str(input("enter name of student:"))
        english=int(input("enter the {name}'s score in english:".format(name=name)))
        science=int(input("enter the {name}'s score in science:".format(name=name)))
        math=int(input("enter the {name}'s score in math:".format(name=name)))
        st_totalscore=english+science+math
        percentage=(st_totalscore/totalscore)*100
        percentage=round(percentage,2)
        passorfail=""
        if english<40 or science<40 or math<40 :
            passorfail="fail"
        else:
            passorfail="pass"


        st_list.append({
            'name':name,
            'english':english,
            'science':science,
            'math':math,
            'st_totalscore':st_totalscore,
            'precentage':round(percentage,2),
            'passorfail':passorfail,
        })
        print("-------------------------------------------")

def overall_cal(st_list):
    engavg=0
    sicavg=0
    mathavg=0
    totalmarks=0
    peravg=0
    for k,v in enumerate(st_list):
        engavg=engavg+v['english']
        sicavg=sicavg+v['science']
        mathavg=mathavg+v['math']
        totalmarks=totalmarks+v['st_totalscore']
        peravg=peravg+v['precentage']


    print("---------overallrecord---------------")
    print("english average marks:",engavg/inp)
    print("science average marks:",sicavg/inp)
    print("math average marks:",mathavg/inp)

    print("totalmarks average marks:",totalmarks/inp)
    print("precentage average :",peravg/inp)

    

def printstrecord():
    for student in st_list:
        print(student)
        

st_record()
printstrecord()
overall_cal(st_list)
i=0
for i in range(i,3):
    print("hello world")


    





