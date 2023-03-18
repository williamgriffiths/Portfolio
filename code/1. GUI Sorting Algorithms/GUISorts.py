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
    
    for i in range(len(nums)): 
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j + 1]: 
                nums[j],nums[j+1] = nums[j+1],nums[j]
                
            window.fill(black) 
            draw(nums,red)
            
            pygame.time.delay(20) 
            pygame.display.update()
            
    draw(nums,green)
    pygame.display.update()
    
    time.sleep(5)
    pygame.quit()



def insertion_sort(nums):
    pygame.display.set_caption("Insertion Sort")
    
    for i in range(len(nums)): 
        key = nums[i]
        j = i-1
        
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
            
        nums[j+1] = key
        window.fill(black) 
        draw(nums,red)
        
        pygame.time.delay(20) 
        pygame.display.update()
        
    draw(nums,green)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()



def selection_sort(nums):
    pygame.display.set_caption("Selection Sort")
    
    for i in range(len(nums)):
        minIndex = i
        
        for j in range(i+1, len(nums)):
            if nums[minIndex] > nums[j]:
                minIndex = j
                
        nums[i],nums[minIndex] = nums[minIndex],nums[i]
        window.fill(black) 
        draw(nums,red)
        
        pygame.time.delay(20) 
        pygame.display.update()
        
    draw(nums,green)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
