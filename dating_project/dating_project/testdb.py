from django.http import HttpResponse

from TestModel.models import CourseDetails

#for insert
# def testdb(request):
#         test1 = CourseDetails(title='test')
#         test1.save()
#         return HttpResponse("<p>add row success!</p>")

#for select
# def testdb(request):
#     #initial
#     response = ""
#     response1 = ""
#
#     #use select * from
#     list = CourseDetails.objects.all()
#
#     #filter like SQL where
#     response2 = CourseDetails.objects.filter(id=1)
#
#     #get the result
#     response3 = CourseDetails.objects.get(id=1)
#
#     #to print out
#     for var in list:
#         response1 += var.duration + " "
#     response = response1
#     return HttpResponse("<p>"+ response +"</p>")


#for update
# def testdb(request):
#     test1 = CourseDetails.objects.get(id=1)
#     test1.title = 'QA'
#     test1.save()
#
#     #another method
#     #Test.objects.filter(id=1).update(title='QA')
#
#     #update all the rows
#     #Test.objects.all().update(title='QA')
#
#     return HttpResponse("<p>updated success.</p>")


#for delete
def testdb(request):
    #delete id = 1 row
    test1 = CourseDetails.objects.get(id=1)
    test1.delete()

    #other method
    #Test.objects.filter(id=1).delete()

    #delete all
    #Test.objects.all().delete()

    return HttpResponse("<p>delete success </p>")