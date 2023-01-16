schedule = list(map(str, input().split(", ")))
while(True):
    line = input().split(":")
    if(line[0] == "course start"):
        break

    command = line[0]

    if(command == "Add"):
        lessonTitle = line[1]
        if(lessonTitle not in schedule):
            schedule.append(lessonTitle)

    elif(command == "Insert"):
        lessonTitle = line[1]
        index = int(line[2])
        if(lessonTitle not in schedule):
            schedule.insert(index, lessonTitle)

    elif(command == "Remove"):
        lessonTitle = line[1]
        index = schedule.index(lessonTitle)
        if(index + 1 < len(schedule)):
            splitted = schedule[index + 1]
            lesson = splitted[0]
            if(lessonTitle == lesson):
                schedule.remove(index + 1)
        if(lessonTitle in schedule):
            schedule.remove(lessonTitle)

    elif(command == "Swap"):
        firstLessonTitle = line[1]
        secondLessonTitle = line[2]
        indexOfFirst = schedule.index(firstLessonTitle)
        indexOfSecond = schedule.index(secondLessonTitle)

        if(indexOfFirst + 1 < len(schedule) and indexOfSecond < len(schedule)):
            firstSplitted = [indexOfFirst + 1]
            secondSplitted = [indexOfSecond + 1]

            firstLesson = firstSplitted[0]
            secondLesson = secondSplitted[0]

            if(firstLessonTitle == firstLesson and secondLessonTitle == secondLesson):
                firstSplitted, secondSplitted = secondSplitted, firstSplitted

        if(firstLessonTitle in schedule and secondLessonTitle in schedule):
            firstLessonTitle, secondLessonTitle = secondLessonTitle, firstLessonTitle

    elif(command == "Exercise"):
        lessonTitle = line[1]
        if(lessonTitle in schedule):
            index = schedule.index(lessonTitle)
            if(index + 1 < len(schedule)):
                nextOne = schedule[index + 1]
                splitted = nextOne.split("-")
                lesson = splitted[0]
                if(lesson != lessonTitle):
                    schedule.insert(index + 1, lessonTitle + "-Exercise")

        else:
            schedule.append(lessonTitle)
            schedule.append(lessonTitle + "-Exercise")
        
counter = 0
for i in schedule:
    counter += 1
    print(f"{counter}.{i}")