{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "076b1540",
   "metadata": {},
   "outputs": [],
   "source": [
    "def class_adder(course_no):\n",
    "    your_rooms = {}\n",
    "    your_teach = {}\n",
    "    your_start = {}\n",
    "    \n",
    "    room = input('Enter the room number: ')\n",
    "    teacher = input('Enter the teacher\\'s name: ')\n",
    "    start = input('Enter the start time of the class: ')\n",
    "    \n",
    "    your_rooms[course_no] = room\n",
    "    your_teach[course_no] = teacher\n",
    "    your_start[course_no] = start\n",
    "    \n",
    "    return your_rooms, your_teach, your_start\n",
    "    \n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    class_adder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aacfa345",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
