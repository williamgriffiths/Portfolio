import pygame
import time

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

width = 960
height = 600
window = pygame.display.set_mode((width,height))
window.fill(black)


def draw(nums,colour):
    for i in range(len(nums)):
        pygame.draw.rect(window,colour,(60+35*i,540-3*nums[i],20,3*nums[i]))


def bubble_sort(nums):
    pygame.display.set_caption("Bubble Sort")
    unsorted = True
    while unsorted:

        for i in range(len(nums)): 
            for j in range(len(nums)-i-1):

                if nums[j] > nums[j + 1]: 
                    nums[j],nums[j+1] = nums[j+1],nums[j]

                window.fill(black) 
                draw(nums,red) 
                pygame.time.delay(20) 
                pygame.display.update()
                
        unsorted = False
        
        draw(nums,green)
        pygame.display.update()
        break

    time.sleep(5)
    pygame.quit()


def insertion_sort(nums):
    pygame.display.set_caption("Insertion Sort")
    unsorted = True
    while unsorted:

        for i in range(len(nums)): 
            for j in range(len(nums)-i): 

                key = nums[j]
                k = j-1
                while k >= 0 and key < nums[k]:
                    nums[k+1] = nums[k]
                    k -= 1
                nums[k+1] = key

                window.fill(black) 
                draw(nums,red) 
                pygame.time.delay(20) 
                pygame.display.update()
                
            unsorted = False
        
            draw(nums,green)
            pygame.display.update()
            break

        time.sleep(5)
        pygame.quit()


def selection_sort(nums):
    pygame.display.set_caption("Selection Sort")
    unsorted = True
    while unsorted:

        for i in range(len(nums)):
            for j in range(len(nums)-i-1):

                minIndex = j
                for k in range(j+1,len(nums)):
                    if nums[minIndex] > nums[k]:
                        minIndex = k
                nums[j],nums[minIndex] = nums[minIndex],nums[j]

                window.fill(black) 
                draw(nums,red) 
                pygame.time.delay(25) 
                pygame.display.update()
                
            unsorted = False
            
            draw(nums,green)
            pygame.display.update()
            break

        time.sleep(5)
        pygame.quit()
