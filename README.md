# webcam_image_changer
Esse programa detecta o vídeo de sua webcam e o altera de várias formas aplicando o processamento de imagem com o opencv.

* Pré-Requisitos
  - Python 3.5
  - Pillow
  - Numpy
  - Opencv
  - Tkinter
 
 * Como usar:
 * Depois de executar o programa você terá que escolher um dos tipos de processamento, representados pelos quatro botões, depois disso será criado uma aba nova, com o vídeo normal na esquerda e o alterado na direita.
   - Canny: O programa pegará o contorno do vídeo e mostrará em preto e branco.
   - Gaussian: O programa irá detectar e mostrar apenas objetos com cores azuis no vídeo.
   - Cascade: O programa tentará achar o seu rosto e colocará um quadrado em volta dele.
   - Laplacian: O programa irá pegar o contorno do vídeo e colocará um gradiente nele 
  

Menu Inicial:

![Captura de tela 2023-05-31 191113](https://github.com/amogushub/webcam_image_changer/assets/134977857/aeb50dcd-9afc-4a30-8303-45efa671df46)

Canny:

![Captura de tela 2023-05-31 190810](https://github.com/amogushub/webcam_image_changer/assets/134977857/60b120a3-8f5f-40b5-b7e8-c683770e1e3d)
