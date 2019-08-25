import requests
from pprint import pprint
url = "http://saral.navgurukul.org/api/courses"
def course(link):
    response=requests.get(link)
    restore=response.json()
#     pprint(restore)
    return restore
full_courses = course(url)
# index=0

# print(full_courses)
courses_list=[]
courses_id_list=[]
# saral_list=(full_courses["AvilableCourses"]
def courses_fun(data_courses):
        index=0

        # print (data_courses)
        while index< len(data_courses["availableCourses"]):
                course_Exercise = full_courses["availableCourses"][index]
                course_name = course_Exercise["name"]
                course_id = course_Exercise["id"]
                courses_list.append(course_name)
                print(str(index+1)+".... "+course_name,course_id)
                courses_id_list.append(course_id)
                # print(courses_id_list)
                # print(course_name)
                index=index+1
        print(courses_id_list)
courses_fun(full_courses)
user_input = int(input("enter your number which course you want : "))
select_id = courses_id_list[user_input - 1]
print (select_id)
url2 = ("http://saral.navgurukul.org/api/courses/"+str(select_id)+"/exercises")
print (url2)
def exercises(url):
        exe_response = requests.get(url)
        exe_store = exe_response.json()
        # print (exe_store)
        return exe_store
full_exercises = exercises(url2)
exercises_list=[]
exercises_slug=[]
exercises_sub_child=[]
def exercises_fun(data_exercises):
        # print(data_exercises)
        index=0
        while index<len(data_exercises["data"]):
                # print (data_exercises)
                exe_data=data_exercises["data"][index]
                # print (exe_data)
                exe_name=exe_data["name"]
                exe_id=exe_data["id"]
                exe_slug=exe_data["slug"]
                # all_exe=exe_data["parentExercisesId"]
                child_ex=exe_data["childExercises"]
                exercises_sub_child.append(child_ex)
                if child_ex!= []:
                        exe_name = exe_data["name"]
                        exe_slug = exe_data["slug"]
                        exercises_list.append(exe_name)
                        print(str(index+1)+".... "+exe_name)
                        exercises_slug.append(exe_slug)
                index=index+1
                # print(child_ex)
        # print(exercises_slug)
exercises_fun(full_exercises)
user_input2 = int(input("enter your number which exercise you want : ")) 
select_slug = exercises_slug[user_input2-1] 
print(select_slug) 
# url3 =("http://saral.navgurukul.org/api/courses/"+str(select_slug)+"/exercises")   
# http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json

url3=url2+"/getBySlug?slug="+select_slug
url3="http://saral.navgurukul.org/api/courses/"+str(select_id)+"/exercise/getBySlug?slug="+select_slug

print(url3)
def lesson_fun(url4):
        # print(urlx)
        lesson_res=requests.get(url4)
        # print (lesson_res)
        lesson_store=lesson_res.json()
        # print(lesson_store)
        return lesson_store
full_content = lesson_fun(url3) 
print (full_content)