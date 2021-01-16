import pygame
import sys
import random
#initlazing the basic  format
pygame.init()
display_width=600
display_height=600
dis=pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('snake game ') # title for snake game

#color selection begins here
color_black ='black'
color_red ='red'
color_blue='blue'
color_green=('green')
color_orange ='orange'
# color_black=(0,0,0)

snake_block=10
snake_list=[]

def snake(snake_block,snake_list):
    for i in snake_list:
        pygame.draw.rect(dis,color_green,[i[0],i[1],snake_block,snake_block])

def snake_game():
    game_over=False
    end_game=False
    x1=display_width/2 #coordinates 
    y1=display_height/2
    x=0
    y=0
    snake_list=[]
    snake_length=1
    add_x=0
    add_y=0
    food_x=round(random.randrange(0,display_width-snake_block)/10.0)*10.0
    food_y=round(random.randrange(0,display_height-snake_block)/10.0)*10.0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
              
                 if pygame.key==pygame.k_LEFT:
                       x=-snake_block
                       y=0
                 elif pygame.key==pygame.k_RIGHT:
                        x=snake_block
                        y=0

                 elif pygame.key==pygame.K_UP:
                        x=-snake_block
                        y=0
                 elif pygame.key==pygame.K_DOWN:
                            x=-snake_block
                            y=0

                       

            if x>= display_width or  x<=0 or y>= display_height or y<0:
                end_game=True
            add_x += x
            add_y += y
            dis.fill(color_orange)
            pygame.draw.rect(dis,color_green,[food_x,food_y],snake_block,snake)
            snake_head=[]
            snake_head.append(x)
            snake_head.append(y)
            snake_list.append(snake_head)
            if len(snake_list>snake_length):
                del snake_list[0]_

            for i in snake_list[:-1]:    
                if x==snake_head:
                    game_end=True
            snake(snake_block,snake_list)        
            pygame.display.update()

pygame.quit()
quit()

            



  
    

        #  pygame.draw.rect(dis,color_green,[200,200,snake_block,snake_block])       



# def main():
#     print('Main function call here ')


# if __name__ == '__main__':
#     main()
#     snake(snake_list,snake_block)
#     snake_game()
    
