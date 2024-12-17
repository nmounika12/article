from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from .models import Article

# Create your views here.
def index(request):
    data=Article.objects.all().order_by('-id')
    if request.method == "POST":
        search = request.POST.get("search")
        data = Article.objects.filter(Q(Article__icontains=search)|Q(description__icontains=search))

        # print(search)
    sub = [i for i in list(data)]
    context = {
        'data':data
    }
# data = [
#     {"id":1, "article": "Royal Challengers Bangalore (RCB) in the IPL: A Saga of Passion and Promise", 
#         "description": "The Royal Challengers Bangalore (RCB) is one of the most talked-about franchises in the Indian Premier League (IPL), not just for its star-studded lineup but also for its ardent fan base and their unyielding loyalty. Despite being one of the most popular teams in the league, RCB is also known for its elusive quest for the IPL title, earning the reputation of being cricket’s perennial underachievers."},

#     {"id":2, "article": "Chennai Super Kings (CSK) in the IPL: The Epitome of Consistency and Glory",
#         "description": "The Chennai Super Kings (CSK) is one of the most successful and iconic franchises in the history of the Indian Premier League (IPL). Known for their yellow jerseys and the roar of their loyal Whistle Podu fan base, CSK has been a benchmark of consistency, leadership, and team spirit. With a remarkable track record and a unique bond with their fans, CSK has cemented its legacy as a powerhouse in T20 cricket.",},

#     {"id":3, "article": "Mumbai Indians (MI) in the IPL: The Undisputed Champions",
#         "description": "The Mumbai Indians (MI) are synonymous with excellence and dominance in the Indian Premier League (IPL). With a record number of titles and a reputation for nurturing talent, MI has set the gold standard for success in T20 cricket. The franchise, often referred to as the Blue and Gold Army, is revered for its strong leadership, strategic brilliance, and unyielding commitment to excellence.",},

#     {"id":4, "article": "Sunrisers Hyderabad (SRH) in the IPL: The Rise of the Orange Army",
#         "description": "The Sunrisers Hyderabad (SRH) is one of the most competitive teams in the Indian Premier League (IPL), known for its consistency, strong bowling attack, and unwavering team spirit. Despite being one of the younger franchises in the league, SRH has left an indelible mark with its focused approach and championship pedigree.",},
    
#     {"id":5, "article": "Kolkata Knight Riders (KKR) in the IPL: The Journey of the Purple and Gold Brigade",
#         "description": "The Kolkata Knight Riders (KKR) is one of the most popular and celebrated franchises in the Indian Premier League (IPL). Known for their vibrant fan base, star-studded ownership, and fearless brand of cricket, KKR has experienced a rollercoaster journey in the league. From struggling in the early seasons to becoming two-time IPL champions, KKR’s story is one of resilience and transformation.",},

#     {"id":6,"article": "Rajasthan Royals (RR) in the IPL: The Journey of the Underdogs",
#         "description": "The Rajasthan Royals (RR) are one of the most intriguing franchises in the Indian Premier League (IPL). Known for their focus on young talent, innovative strategies, and an underdog spirit, RR has carved out a unique identity in the league. Despite a mix of highs and lows, the Royals remain a respected and admired team in the IPL ecosystem",},

#     {"id":7, "article": "Lucknow Super Giants (LSG) in the IPL: A Promising New Entrant",
#         "description": "The Lucknow Super Giants (LSG), one of the two newest franchises in the Indian Premier League (IPL), has quickly established itself as a competitive team. Representing Lucknow, the capital of Uttar Pradesh, LSG was introduced in the IPL during the 2022 season alongside the Gujarat Titans. Despite being new, the team has shown promise with its balanced squad, tactical leadership, and impressive performances.",},

#     {"id":8, "article": "Delhi Capitals (DC) in the IPL: A Tale of Resilience and Ambition",
#         "description": "Delhi Capitals (DC), one of the most prominent franchises in the Indian Premier League (IPL), has been a team of promise and potential, even though they have yet to capture the coveted IPL title. Known for their blend of youth and experience, DC has consistently competed at a high level, reaching the playoffs multiple times and coming close to winning the title. Their journey in the IPL reflects both the highs of emerging talent and the struggles of maintaining consistency.",},

#     {"id":9, "article": "The Importance of Education in Society",
#         "description": "Education plays a crucial role in shaping individuals and driving societal progress",},

  
# ]


    return render(request,'index.html',context)

def details(request,pk):
    data1=Article.objects.get(id=pk)
    context = {
        'data1':data1
    }
    return render(request,'single.html',context)
