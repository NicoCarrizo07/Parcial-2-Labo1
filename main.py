import pygame
from pygame.locals import *
from config import *
from player import *
from sprite_sheet import SpriteSheet
from plataforma import *
from random import *
from disparo import *
from monedas import Moneda
from lava import *
from plataforma_movil import *
from enemigo import *
from vida import *
from reloj import *
from guardar_puntaje import *
from door import *
from boss import *
from meteoritos import *

def wait_user_clik_comenzar(screen,rect_comenzar:pygame.Rect,rect_salir:pygame.Rect,rect_instrucciones:pygame.Rect):
            """Pausar el juego hasta que el jugador haga clik en pantalla

            Args:
                rect_comenzar: rectangulo donde si haces clik el juego comienza
                rect_salir: rectangulo donde si haces clik el juego muestra los comandos
                rect_instrucciones : rectangulo donde si haces clik el juego comienza finaliza

            Returns:
                None
            """
            while True:
                crear_boton(screen,rect_comenzar,"Comenzar",BLUE,GREEN)
                crear_boton(screen,rect_instrucciones,"Comandos",BLUE,GREEN)
                crear_boton(screen,rect_salir,"Salir",BLUE,GREEN)
                pygame.display.flip() #PINTAR PANTALLA
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminar()

                    if event.type == KEYDOWN: #evento presionar tecla
                        if event.key == K_ESCAPE:
                            terminar()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if rect_comenzar.collidepoint(event.pos):
                                #click_sound.play()
                                return None
                            elif rect_salir.collidepoint(event.pos):
                                #click_sound.play()
                                terminar()
                            elif rect_instrucciones.collidepoint(event.pos):
                                #click_sound.play()
                                screen.blit(imagen_instrucciones, (0,0))
                                pygame.display.flip() #PINTAR PANTALLA
                                wait_user()
                                return None

class Game:
    def __init__(self): #inicializar atributos(caracterisitcas)
        pygame.init()
        pygame.mixer.music.load(r"Clase23 Video copy 2\assets\sounds\musica fondo.mp3")
        pygame.mixer.music.set_volume(0.1)
        self.sound_coin = pygame.mixer.Sound(r"Clase23 Video copy 2\assets\sounds\moneda sound.mp3")
        self.fuente = pygame.font.SysFont(None,50)#(fuente,tamanio)crear obejeto de la clase fuente
        click_sound = pygame.mixer.Sound(r"Parcial Entrega\Sonidos\mouse-click-153941.mp3")
        self.herida = pygame.mixer.Sound(r"Clase23 Video copy 2\assets\sounds\herida.mp3")
        self.game_over_sound = pygame.mixer.Sound(r"Clase23 Video copy 2\assets\sounds\game_over.mp3")
        self.vida_sound = pygame.mixer.Sound(r"Clase23 Video copy 2\assets\sounds\vida_extra.mp3")
        self.victory_sound = pygame.mixer.Sound(r"Clase23 Video copy 2\assets\sounds\success-fanfare-trumpets-6185.mp3")
        
        #configuraciones de pantalla
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Dragon Game") #titulo
        pygame.display.set_icon(pygame.image.load(r"Clase23 Video copy 2\assets\images\drag_wl_5.png"))
        
        self.level_one = True
        self.level_two = False

        self.all_sprites = pygame.sprite.Group() #grupo de sprites
        self.platforms= pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()
        self.proyectiles = pygame.sprite.Group()
        self.lives_group = pygame.sprite.Group()
        self.timer_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group() 
        self.boss_group = pygame.sprite.Group()
        self.meteoritos_group = pygame.sprite.Group()  
        sprite_sheet_player =  SpriteSheet(pygame.image.load
        (r"Clase23 Video copy 2\assets\images\dragon1 (1) (2).png").convert_alpha(),4,9,320,320,
        ["right","left","front","back"])#filas,columnas,ancho lo saco con la app,alto

        self.platform1 = Platform([self.all_sprites, self.platforms], (300,500,200,50))
        self.platform2 = Platform([self.all_sprites, self.platforms], (600, 475, 150, 50))
        self.platform3 = Platform([self.all_sprites, self.platforms], (300, 300, 100, 50))
        self.platform4 = Platform([self.all_sprites, self.platforms], (450, 100, 100, 50))
        self.platform5 = Platform([self.all_sprites, self.platforms], (600, 370, 150, 50))
        self.platform6 = Platform([self.all_sprites, self.platforms], (650, 165, 138, 50))

        self.imagen_visible_parlante = False
        self.playing_music = True

        self.player = Player([self.all_sprites],sprite_sheet_player)#le paso el grupo al que pertenece
        self.enemy = Enemigo([self.all_sprites,self.enemies_group], self.platform1, r"Clase23 Video copy 2\assets\images\s0.png")
        self.enemy2 = Enemigo([self.all_sprites,self.enemies_group], self.platform2, r"Clase23 Video copy 2\assets\images\s0.png")
        self.enemy3 = Enemigo([self.all_sprites,self.enemies_group], self.platform5, r"Clase23 Video copy 2\assets\images\s0.png")
        
        self.enemy1_muerto = False
        self.enemy2_muerto = False
        self.enemy3_muerto = False

        self.image_sequence_money = [
            pygame.image.load(r'Clase23 Video copy 2\assets\images\monedas\Coin1.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\monedas\Coin2.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\monedas\Coin3.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\monedas\Coin4.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\monedas\Coin5.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\monedas\Coin6.png')
        ]

        self.image_sequence_life = [
            pygame.image.load(r'Clase23 Video copy 2\assets\images\corazon\c0.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\corazon\c1.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\corazon\c2.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\corazon\c3.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\corazon\c4.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\corazon\c5.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\corazon\c6.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\corazon\c7.png')
        ]

        self.door_images = [
            pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\puerta\0.png").convert_alpha(),(80,80)),
            pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\puerta\1.png").convert_alpha(),(80,80)),
            pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\puerta\2.png").convert_alpha(),(80,80)),
            pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\puerta\3.png").convert_alpha(),(80,80))
        ]

        self.door = Door(self.door_images)
        self.door.visible = True 
        
        self.image_sequence_boss = [
            pygame.image.load(r'Clase23 Video copy 2\assets\images\boss\3.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\boss\4.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\boss\5.png'),
            pygame.image.load(r'Clase23 Video copy 2\assets\images\boss\6.png')
        ]


        # Variables para controlar la animación
        self.current_frame = 0
        self.animation_speed = 7 
        self.timer = 0

        self.contador = 0
        texto = self.fuente.render(f"Score : {self.contador}",True, WHITE)
        self.rect_texto = texto.get_rect()
        self.rect_texto.midtop = (WIDTH //2 , 30)

        self.vidas = 3
        self.texto_vidas = self.fuente.render(f"Vidas: {self.vidas}", True, WHITE)
        self.rect_texto_vidas = self.texto_vidas.get_rect(topright=(WIDTH - 30, 30))

        buttom_width = 200
        buttom_height = 50

        self.buttom_comenzar = pygame.Rect(0,0,buttom_width,buttom_height)
        self.buttom_comenzar.center = (CENTER_SCREEN)

        self.button_salir = pygame.Rect(0, 0, buttom_width, buttom_height)
        self.button_salir.center = (CENTER_SCREEN[0], CENTER_SCREEN[1] + buttom_height + 20)

        self.buttom_instrucciones = pygame.Rect(0,0,buttom_width,buttom_height)
        self.buttom_instrucciones.center = (CENTER_SCREEN[0], CENTER_SCREEN[1] + 2 * buttom_height + 40)

        self.can_shoot = True 
        self.shoot_timer = 0  #temporizador de disparo

        platform_image = pygame.image.load(r'Clase23 Video copy 2\assets\images\2dplatform.png').convert_alpha()
        imagen_achicada = pygame.transform.scale(platform_image, (platform_image.get_width() // 8, platform_image.get_height() // 8))
        self.platform_movil = PlataformaMovil([self.all_sprites, self.platforms], (50, 300, 100, 50), imagen_achicada)

        self.tiempo_restante = 100  #segundos del juego
        self.fuente_temporizador = pygame.font.SysFont(None, 36)
        self.color_temporizador = (255, 255, 255)  

        self.boss = Boss([self.boss_group],30,490,self.image_sequence_boss,2) 
    
        self.boss_dibujado = True
        self.contador_boss_muerto = 0

        
        self.tiempo_caida_meteorito = 0
        self.cooldown_caida = 4000  # 3000 milisegundos


    def generar_monedas(self, cantidad=5):
        for _ in range(cantidad):
            x = random.randint(10, WIDTH-50)  #
            y = random.randint(10, HEIGHT-80 )  
            coin = Moneda(x, y, self.image_sequence_money) 
            self.coins_group.add(coin)

        for _ in range(1):
            life = Vida(500, 65, self.image_sequence_life)  
            self.lives_group.add(life)
        
        for _ in range(1):
            reloj = Reloj(335, 283)  
            self.timer_group.add(reloj)

        if self.level_two:
            for _ in range(1):
                reloj = Reloj(100, 290)  
                self.timer_group.add(reloj)

    def run(self):

        while True:
            self.screen.blit(imagen_dragon_fondo, (0,0))
            mostrar_texto(self.screen,"Dragon Game",self.fuente,(WIDTH//2,20),GREEN,BLACK) #WIDTH//2 mitad  de la pantalla
            mostrar_texto(self.screen,"Nivel 1",self.fuente,(WIDTH//2,70),GREEN,BLACK) #WIDTH//2 mitad  de la pantalla
            wait_user_clik_comenzar(self.screen, self.buttom_comenzar, self.button_salir, self.buttom_instrucciones)
            
            running = True
            
            self.tiempo_restante = 100  
            self.fuente_temporizador = pygame.font.SysFont(None, 36)
            self.color_temporizador = (255, 255, 255) 
            pygame.mixer.music.play(0)
            direction = "right"  # inicializa la dirección derecha
            self.generar_monedas()
            if self.level_one:
                self.screen.blit(self.door.image, self.door.rect)
            
            if self.level_two:
                print("entre")
                

            while running:
                
                self.clock.tick(FPS)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    
                    if event.type == KEYDOWN:
                        if event.key == K_p:
                            if self.playing_music:
                                pygame.mixer.music.pause()
                            mostrar_texto(self.screen,"Pausa",self.fuente,CENTER_SCREEN,WHITE,BLACK)
                            pygame.display.flip()
                            wait_user()
                            if self.playing_music:
                                pygame.mixer.music.unpause()
                        if event.key == K_m:
                            self.imagen_visible_parlante = not self.imagen_visible_parlante
                            if self.playing_music:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()

                            self.playing_music = not self.playing_music

                        if event.key ==K_SPACE:
                            self.player.jump()
                        if event.key == K_f:
                            if self.can_shoot:  #verifica si se puede disparar
                                Proyectil([self.all_sprites, self.proyectiles], self.player.rect.center, direction)
                                self.can_shoot = False 
                                self.shoot_timer = pygame.time.get_ticks()  #obtener el tiempo actual

                    if event.type == KEYUP:
                        if event.key == K_ESCAPE:
                            terminar()

                keys = pygame.key.get_pressed()
                if keys[K_RIGHT]:
                    direction = "right"
                elif keys[K_LEFT]:
                    direction = "left"

                if not self.can_shoot:
                    if pygame.time.get_ticks() - self.shoot_timer > 250:  #tiempo_entre_disparos es el tiempo en milisegundos
                        self.can_shoot = True  #habilita el disparo nuevamente

                self.timer += self.clock.get_rawtime()
                if self.timer >= self.animation_speed:
                    self.timer = 0
                    self.current_frame = (self.current_frame + 1) % len(self.image_sequence_money)

                if self.level_one == True:
                    self.lava_image = pygame.image.load(r'Clase23 Video copy 2\assets\images\lava 1.png').convert_alpha()
                    self.lava = Lava(x=0 , y=500, image=self.lava_image)

                if self.level_one ==True:
                    self.lava.check_collision(self.player)
                    self.lava.draw(self.screen)

                self.coins_group.update()  #monedas

                self.lives_group.update()  #vidas

                if self.level_one:
                    self.platforms.draw(self.screen)

                if self.level_one:
                    self.platform_movil.update() 
                    self.platform_movil.draw(self.screen)  

                self.enemies_group.update() 
    
                self.actualizar_temporizador()
                if self.tiempo_restante <= 0:
                    puntaje_obtenido = self.contador
                    self.screen.blit(imagen_muerte, (0,0))
                    self.game_over_sound.play()
                    pygame.mixer.music.stop()
                    mostrar_texto(self.screen,"Game over",self.fuente,(WIDTH//2,20),WHITE)
                    mostrar_texto(self.screen,"Precione una tecla para guardar puntaje",self.fuente,(WIDTH//2,HEIGHT//2),WHITE)
                    mostrar_texto(self.screen,f"Su puntuacion fue : {self.contador}",self.fuente,(WIDTH//2,HEIGHT - 30),WHITE)
                    pygame.display.flip()
                    wait_user()
                    guardar = GuardarPuntaje("puntajes.json") 
                    guardar.finalizar_juego(puntaje_obtenido)
                    terminar()

                if self.enemy1_muerto and self.enemy2_muerto and self.enemy3_muerto:
                    self.door.activate()
                    if pygame.sprite.collide_rect(self.player, self.door):
                        self.screen.blit(fondo, (0,0))
                        self.victory_sound.play()
                        self.level_one = False
                        self.level_two = True
                        mostrar_texto(self.screen,"Nivel 1 completo",self.fuente,(WIDTH//2,20),WHITE)
                        mostrar_texto(self.screen,"Precione una tecla para pasar de nivel",self.fuente,(WIDTH//2,HEIGHT//2),WHITE)
                        pygame.display.flip()
                        self.reset_enemies()
                        self.level_one = False
                        self.level_two = True
                        self.eliminar_platforms()
                        pygame.display.flip()
                        wait_user()

                if self.level_two: #boss
                    if self.boss_dibujado == True:
                        self.boss.update()  
                        self.boss.draw(self.screen)  
                        pygame.display.flip()

                if self.level_two: #meteortio
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - self.tiempo_caida_meteorito > self.cooldown_caida:
                        meteorito = Meteorito()  #instancia de meteorito
                        self.meteoritos_group.add(meteorito)  
                        self.tiempo_caida_meteorito = tiempo_actual  

                    self.meteoritos_group.update()  
                    self.meteoritos_group.draw(self.screen) 

                    colisiones_meteorito_jugador = pygame.sprite.spritecollide(self.player, self.meteoritos_group, True)
                    for meteorito in colisiones_meteorito_jugador:
                        self.vidas -= 1  
                        self.herida.play()
                        if self.vidas ==0:
                            puntaje_obtenido = self.contador  
                            self.screen.blit(imagen_muerte, (0,0))
                            self.game_over_sound.play()
                            pygame.mixer.music.stop()
                            mostrar_texto(self.screen,"Game over",self.fuente,(WIDTH//2,20),WHITE)
                            mostrar_texto(self.screen,"Precione una tecla para guardar puntaje",self.fuente,(WIDTH//2,HEIGHT//2),WHITE)
                            pygame.display.flip()
                            wait_user()
                            guardar = GuardarPuntaje("puntajes.json")  
                            guardar.finalizar_juego(puntaje_obtenido)
                            terminar() 


                if self.level_one:
                    if self.door.active and not self.door.visible:
                        self.door.update()
                        self.screen.blit(self.door.image, self.door.rect)

                pygame.display.flip()

                self.update()
                self.draw()

            self.close()

    def actualizar_temporizador(self):
        segundos_transcurridos = self.clock.get_time() / 1000 
        self.tiempo_restante -= segundos_transcurridos

    def draw(self):
        
        self.screen.blit(fondo, (0,0))

        if self.level_one:
            self.platforms.draw(self.screen)

        self.all_sprites.draw(self.screen)

        self.coins_group.draw(self.screen)
        self.lives_group.draw(self.screen)
        self.timer_group.draw(self.screen)

        if self.imagen_visible_parlante:
            self.screen.blit(imagen_parlante_reescalada,(60, 90))

        texto = self.fuente.render(f"Score: {self.contador}", True, BLACK)
        self.screen.blit(texto, self.rect_texto)

        self.screen.blit(self.texto_vidas, self.rect_texto_vidas)

        texto_temporizador = self.fuente_temporizador.render(
            f"Tiempo: {max(0, int(self.tiempo_restante))} s", True, self.color_temporizador)
        self.screen.blit(texto_temporizador, (10, 30))

        for enemy in self.all_sprites:
            if isinstance(enemy, Enemigo):
                for proyectil in enemy.proyectiles:
                    proyectil_image, proyectil_rect = proyectil
                    self.screen.blit(proyectil_image, proyectil_rect)
        
        if self.level_two:
            for boss in self.boss_group:
                if isinstance(boss, Boss):
                    for proyectil in boss.proyectiles:
                        proyectil_image, proyectil_rect = proyectil
                        self.screen.blit(proyectil_image, proyectil_rect) 

    def update(self):

        self.texto_vidas = self.fuente.render(f"Vidas: {self.vidas}", True, WHITE)

        plataformas = pygame.sprite.spritecollide(self.player,self.platforms,False, pygame.sprite.collide_mask)#plataforma con la q choco el player

        for plataforma in plataformas:
            if self.player.rect.bottom >= plataforma.rect.top and self.player.speed_vertical > 0:
                self.player.rect.bottom = plataforma.rect.top +16 
                self.player.speed_vertical = 0

        coins_collected = pygame.sprite.spritecollide(self.player, self.coins_group, True, pygame.sprite.collide_mask)

        for coin in coins_collected:
            if self.playing_music:  
                self.sound_coin.play()
            self.contador +=1

        lifes_collected = pygame.sprite.spritecollide(self.player, self.lives_group, True, pygame.sprite.collide_mask)

        for life in lifes_collected:
            if self.playing_music:  
                self.vida_sound.play()
            self.vidas +=1

        timer_collected = pygame.sprite.spritecollide(self.player, self.timer_group, True, pygame.sprite.collide_mask)

        for tiempo in timer_collected:
            if self.playing_music:  #varificar si el juego está en modo silencioso
                self.sound_coin.play()
            self.tiempo_restante +=30

        for enemy in self.all_sprites:
            if isinstance(enemy, Enemigo): #si el objeto enemy es una instancia de la clase Enemigo
                for proyectil in enemy.proyectiles:
                    if proyectil[1].colliderect(self.player.rect):
                        self.vidas -= 1  
                        self.herida.play()
                        if self.vidas ==0:
                            puntaje_obtenido = self.contador  
                            self.screen.blit(imagen_muerte, (0,0))
                            self.game_over_sound.play()
                            pygame.mixer.music.stop()
                            mostrar_texto(self.screen,"Game over",self.fuente,(WIDTH//2,20),WHITE)
                            mostrar_texto(self.screen,"Precione una tecla para guardar puntaje",self.fuente,(WIDTH//2,HEIGHT//2),WHITE)
                            pygame.display.flip()
                            wait_user()
                            guardar = GuardarPuntaje("puntajes.json")  
                            guardar.finalizar_juego(puntaje_obtenido)
                            terminar()
                        enemy.proyectiles.remove(proyectil)
                        break  # sale del bucle para evitar mas colisiones en este fotograma
        if self.level_two:
            for boss in self.boss_group:
                if isinstance(boss, Boss):
                    for proyectil in boss.proyectiles:
                        if proyectil[1].colliderect(self.player.rect):  #colision entre proyectil y jugador
                            self.vidas -= 1  
                            self.herida.play()
                            if self.vidas ==0:
                                puntaje_obtenido = self.contador  
                                self.screen.blit(imagen_muerte, (0,0))
                                self.game_over_sound.play()
                                pygame.mixer.music.stop()
                                mostrar_texto(self.screen,"Game over",self.fuente,(WIDTH//2,20),WHITE)
                                mostrar_texto(self.screen,"Precione una tecla para guardar puntaje",self.fuente,(WIDTH//2,HEIGHT//2),WHITE)
                                pygame.display.flip()
                                wait_user()
                                guardar = GuardarPuntaje("puntajes.json")  # Reemplaza "puntajes.json" con el nombre de tu archivo
                                guardar.finalizar_juego(puntaje_obtenido)
                                terminar()
                            # Eliminar el proyectil
                            boss.proyectiles.remove(proyectil)
                            break  # Salir del bucle para evitar más colisiones en este fotograma

        if self.level_two == True:

            boss_muerto = pygame.sprite.groupcollide(self.boss_group, self.proyectiles, False, True)

            for boss in boss_muerto:
                self.contador_boss_muerto += 1
                print(self.contador_boss_muerto)
                self.contador += 10
                if self.contador_boss_muerto == 10:
                    self.all_sprites.remove(self.proyectiles)
                    self.boss_dibujado = False
                    puntaje_obtenido = self.contador
                    self.screen.blit(imagen_victory, (0,0))
                    self.victory_sound.play()
                    #pygame.mixer.music.stop()
                    mostrar_texto(self.screen,"Felicitaciones, juego completo!",self.fuente,(WIDTH//2,20),WHITE)
                    mostrar_texto(self.screen,"Precione una tecla para guardar puntaje",self.fuente,(WIDTH//2,HEIGHT//2),WHITE)
                    mostrar_texto(self.screen,f"Su puntuacion fue : {self.contador}",self.fuente,(WIDTH//2,HEIGHT - 30),WHITE)
                    pygame.display.flip()
                    wait_user()
                    guardar = GuardarPuntaje("puntajes.json")
                    guardar.finalizar_juego(puntaje_obtenido)
                    terminar()
                    #break # Salir del bucle

        if self.level_one == True:
            enemigo_muerto = pygame.sprite.spritecollide( self.enemy,self.proyectiles, True, pygame.sprite.collide_mask)
        
            for enemy in enemigo_muerto:
                self.contador +=5
                self.enemy.kill()
                self.enemy1_muerto = True
                self.enemies_group.remove(enemy)  # Elimina al enemigo del grupo de sprites
                self.all_sprites.remove(enemy)

        if self.level_one == True:
            enemigo_muerto2 = pygame.sprite.spritecollide( self.enemy2,self.proyectiles, True, pygame.sprite.collide_mask)
            for enemy2 in enemigo_muerto2:
                self.contador +=5
                self.enemy2.kill()
                self.enemy2_muerto = True
                self.enemies_group.remove(enemy2)  # Elimina al enemigo del grupo de sprites
                self.all_sprites.remove(enemy2)

        if self.level_one == True:
            enemigo_muerto3 = pygame.sprite.spritecollide( self.enemy3,self.proyectiles, True, pygame.sprite.collide_mask)
            for enemy3 in enemigo_muerto3:
                self.contador +=5
                self.enemy3.kill()
                self.enemy3_muerto = True
                self.enemies_group.remove(enemy3)  # Elimina al enemigo del grupo de sprites
                self.all_sprites.remove(enemy3)

        if self.enemy1_muerto and self.enemy2_muerto and self.enemy3_muerto:
            self.door.activate()

        self.all_sprites.update()

        pygame.display.flip()

    def reset_enemies(self):
        self.enemy1_muerto = False
        self.enemy2_muerto = False
        self.enemy3_muerto = False

    def close(self):
        pygame.quit()

    def eliminar_platforms(self):
        self.platforms.remove(self.platform1)
        self.platforms.remove(self.platform2)
        self.platforms.remove(self.platform3)
        self.platforms.remove(self.platform4)
        self.platforms.remove(self.platform5)
        self.platforms.remove(self.platform6)
        self.platforms.remove(self.platform_movil)
        self.platform_movil.kill()
        self.platform1.kill()
        self.platform2.kill()
        self.platform3.kill()
        self.platform4.kill()
        self.platform5.kill()
        self.platform6.kill()


if __name__ == "__main__": #se ejecuta solo desde el main,desde otro archivo no
    #game = objeto , Game() = clase
    game = Game() #crear objeto game 
    game.run()#llamo al metodo run para que se ejecute
