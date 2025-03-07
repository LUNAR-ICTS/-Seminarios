# Roadmap:
# 0 - O que é uma imagem?

Uma imagem digital é composta por três canais de cores (Vermelho, Verde e Azul - RGB), cada um representado por uma matriz bidimensional onde os valores indicam a intensidade da cor em cada pixel. A sobreposição dessas matrizes forma uma estrutura tridimensional $(altura, largura, 3)$, permitindo a composição das cores e a exibição da imagem.

<div style="display: inline_block" align="center">
<img height="200cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Creeper_mine_painting.png?raw=true"/> 

<em><b>Figura 1:</b> Pintura Creebet do Minecraft. [<a href="#1-mojang-ref">1</a>]</em>
</div>

<div style="display: inline_block" align="center">
<img height="160cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Creeper_mine_painting_R.png?raw=true"/> 
<img height="160cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Creeper_mine_painting_G.png?raw=true"/> 
<img height="160cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Creeper_mine_painting_B.png?raw=true"/>  
<em><b>Figura 2:</b> Canais da Figura 1 separados (Vermelho, Verde e Azul - RGB). </em>
</div>

<br>

**$$R_{16x32}:$$**

$$
\begin{bmatrix} 
 76 & 71 & 67 & 77 & 70 & 68 & 70 & 70 & 71 & 71 & 71 & 71 & 71 & 70 & 69 & 67 & 67 & 75 & 88 & 86 & 84 & 81 & 81 & 85 & 84 & 83 & 85 & 81 & 78 & 78 & 86 & 78 & \\
 73 & 152 & 120 & 113 & 15 & 4 & 8 & 4 & 3 & 3 & 4 & 7 & 7 & 7 & 9 & 13 & 20 & 78 & 164 & 148 & 136 & 145 & 139 & 156 & 163 & 170 & 173 & 150 & 198 & 208 & 192 & 77 & \\
 84 & 169 & 126 & 119 & 7 & 0 & 2 & 12 & 18 & 16 & 9 & 0 & 0 & 5 & 73 & 139 & 163 & 123 & 57 & 63 & 83 & 193 & 183 & 138 & 160 & 188 & 182 & 210 & 219 & 229 & 206 & 76 & \\
 85 & 170 & 131 & 111 & 11 & 0 & 32 & 136 & 176 & 152 & 113 & 27 & 21 & 58 & 167 & 204 & 190 & 160 & 140 & 117 & 129 & 166 & 184 & 189 & 201 & 166 & 180 & 215 & 218 & 225 & 205 & 85 & \\
 84 & 169 & 137 & 114 & 40 & 14 & 32 & 26 & 23 & 27 & 84 & 91 & 86 & 87 & 93 & 116 & 140 & 146 & 147 & 46 & 80 & 153 & 193 & 142 & 123 & 102 & 199 & 210 & 220 & 223 & 204 & 88 & \\
 85 & 171 & 132 & 119 & 35 & 8 & 63 & 66 & 76 & 68 & 64 & 74 & 90 & 96 & 109 & 141 & 131 & 120 & 59 & 78 & 73 & 110 & 92 & 103 & 105 & 190 & 152 & 197 & 219 & 224 & 204 & 88 & \\
 84 & 171 & 128 & 108 & 43 & 4 & 43 & 68 & 59 & 16 & 27 & 66 & 93 & 79 & 150 & 195 & 185 & 142 & 67 & 36 & 56 & 134 & 84 & 30 & 66 & 198 & 140 & 189 & 221 & 223 & 211 & 88 & \\
 84 & 168 & 122 & 104 & 48 & 21 & 18 & 54 & 14 & 37 & 137 & 127 & 198 & 143 & 34 & 86 & 133 & 81 & 76 & 34 & 22 & 93 & 69 & 19 & 31 & 122 & 179 & 126 & 211 & 227 & 208 & 86 & \\
 85 & 166 & 123 & 118 & 72 & 56 & 8 & 39 & 69 & 95 & 121 & 110 & 155 & 169 & 163 & 168 & 127 & 98 & 127 & 102 & 122 & 35 & 38 & 155 & 82 & 93 & 96 & 168 & 214 & 224 & 204 & 86 & \\
 85 & 166 & 126 & 106 & 15 & 8 & 3 & 15 & 32 & 21 & 15 & 58 & 74 & 87 & 145 & 126 & 137 & 135 & 158 & 90 & 58 & 2 & 0 & 43 & 106 & 156 & 33 & 194 & 217 & 220 & 202 & 87 & \\
 85 & 162 & 117 & 105 & 8 & 32 & 18 & 127 & 134 & 107 & 82 & 60 & 123 & 11 & 6 & 48 & 13 & 19 & 167 & 103 & 5 & 8 & 9 & 4 & 85 & 86 & 29 & 107 & 206 & 219 & 200 & 87 & \\
 83 & 151 & 109 & 114 & 23 & 14 & 23 & 105 & 91 & 38 & 157 & 78 & 70 & 18 & 11 & 18 & 12 & 19 & 111 & 126 & 46 & 134 & 154 & 48 & 69 & 101 & 22 & 31 & 196 & 216 & 197 & 87 & \\
 83 & 153 & 114 & 125 & 175 & 178 & 175 & 99 & 102 & 139 & 111 & 89 & 135 & 181 & 189 & 185 & 196 & 191 & 197 & 198 & 194 & 176 & 184 & 202 & 203 & 199 & 191 & 191 & 207 & 208 & 189 & 86 & \\
 81 & 157 & 173 & 181 & 181 & 179 & 181 & 175 & 176 & 182 & 174 & 174 & 186 & 196 & 188 & 188 & 192 & 193 & 195 & 197 & 199 & 192 & 196 & 199 & 205 & 197 & 198 & 202 & 199 & 197 & 188 & 84 & \\
 81 & 148 & 161 & 162 & 154 & 159 & 164 & 160 & 164 & 175 & 168 & 170 & 167 & 169 & 173 & 164 & 171 & 166 & 175 & 176 & 175 & 177 & 180 & 175 & 178 & 174 & 179 & 176 & 180 & 177 & 168 & 83 & \\
 77 & 71 & 70 & 80 & 80 & 81 & 82 & 81 & 81 & 84 & 83 & 83 & 83 & 82 & 83 & 82 & 83 & 83 & 85 & 85 & 85 & 85 & 85 & 85 & 84 & 84 & 85 & 84 & 76 & 76 & 83 & 79 & \\     
\end{bmatrix}
$$


**$$G_{16x32}:$$**

$$
\begin{bmatrix}
 45 & 37 & 31 & 38 & 35 & 35 & 36 & 36 & 38 & 44 & 45 & 43 & 44 & 54 & 56 & 55 & 56 & 61 & 58 & 57 & 56 & 54 & 54 & 56 & 50 & 51 & 53 & 51 & 45 & 47 & 64 & 49 & \\     
 39 & 145 & 104 & 101 & 70 & 61 & 65 & 58 & 58 & 58 & 63 & 60 & 60 & 64 & 80 & 89 & 96 & 147 & 194 & 182 & 178 & 183 & 181 & 190 & 195 & 199 & 197 & 180 & 197 & 201 & 166 & 43 & \\
 49 & 164 & 115 & 112 & 103 & 106 & 113 & 108 & 98 & 92 & 94 & 108 & 104 & 106 & 144 & 187 & 201 & 186 & 167 & 151 & 159 & 219 & 216 & 196 & 205 & 219 & 214 & 225 & 219 & 226 & 183 & 41 & \\
 50 & 161 & 116 & 104 & 121 & 127 & 137 & 183 & 201 & 189 & 168 & 139 & 138 & 147 & 198 & 222 & 214 & 202 & 197 & 187 & 188 & 204 & 215 & 220 & 223 & 204 & 210 & 223 & 216 & 222 & 185 & 50 & \\
 54 & 161 & 122 & 105 & 130 & 131 & 138 & 140 & 143 & 141 & 159 & 167 & 169 & 169 & 167 & 177 & 191 & 194 & 199 & 178 & 182 & 198 & 208 & 223 & 205 & 163 & 220 & 222 & 221 & 220 & 184 & 56 & \\
 54 & 164 & 116 & 108 & 135 & 135 & 152 & 152 & 159 & 158 & 159 & 163 & 169 & 174 & 179 & 191 & 188 & 183 & 159 & 183 & 180 & 194 & 159 & 205 & 188 & 204 & 202 & 221 & 220 & 220 & 186 & 48 & \\
 64 & 165 & 112 & 99 & 139 & 141 & 151 & 157 & 155 & 148 & 156 & 160 & 171 & 169 & 194 & 217 & 212 & 196 & 184 & 94 & 94 & 202 & 157 & 80 & 100 & 209 & 196 & 213 & 222 & 220 & 195 & 49 & \\
 64 & 162 & 109 & 94 & 146 & 148 & 148 & 154 & 146 & 161 & 192 & 188 & 219 & 192 & 128 & 160 & 182 & 157 & 193 & 85 & 34 & 188 & 167 & 29 & 67 & 199 & 213 & 179 & 215 & 222 & 193 & 65 & \\
 55 & 163 & 110 & 108 & 144 & 152 & 135 & 145 & 158 & 174 & 186 & 179 & 197 & 205 & 201 & 203 & 183 & 164 & 201 & 179 & 181 & 85 & 85 & 177 & 151 & 201 & 167 & 200 & 215 & 220 & 185 & 64 & \\
 53 & 165 & 114 & 96 & 108 & 117 & 119 & 127 & 140 & 129 & 128 & 145 & 157 & 164 & 188 & 183 & 185 & 183 & 204 & 153 & 92 & 4 & 2 & 93 & 204 & 199 & 120 & 212 & 215 & 217 & 181 & 56 & \\
 54 & 159 & 104 & 96 & 115 & 127 & 129 & 167 & 153 & 125 & 112 & 101 & 162 & 92 & 72 & 124 & 110 & 79 & 211 & 159 & 14 & 12 & 11 & 18 & 173 & 161 & 117 & 163 & 207 & 214 & 178 & 55 & \\
 61 & 147 & 96 & 102 & 101 & 88 & 107 & 131 & 100 & 66 & 170 & 107 & 92 & 31 & 26 & 48 & 67 & 83 & 208 & 206 & 83 & 185 & 188 & 90 & 147 & 192 & 114 & 135 & 203 & 212 & 176 & 53 & \\
 56 & 144 & 100 & 107 & 177 & 186 & 185 & 130 & 131 & 159 & 141 & 131 & 155 & 181 & 188 & 187 & 199 & 195 & 203 & 203 & 202 & 188 & 196 & 208 & 208 & 202 & 195 & 199 & 207 & 206 & 166 & 45 & \\
 51 & 147 & 161 & 167 & 168 & 170 & 172 & 166 & 168 & 172 & 164 & 163 & 171 & 180 & 169 & 168 & 172 & 171 & 173 & 176 & 178 & 172 & 178 & 179 & 187 & 178 & 178 & 180 & 180 & 177 & 164 & 47 & \\
 45 & 139 & 152 & 148 & 140 & 147 & 151 & 144 & 148 & 160 & 154 & 153 & 148 & 153 & 157 & 147 & 153 & 145 & 154 & 156 & 156 & 159 & 162 & 156 & 159 & 155 & 160 & 158 & 159 & 155 & 148 & 55 & \\
 45 & 37 & 35 & 42 & 41 & 43 & 44 & 43 & 45 & 52 & 52 & 51 & 52 & 62 & 64 & 62 & 63 & 62 & 54 & 53 & 53 & 53 & 54 & 53 & 46 & 48 & 51 & 50 & 42 & 43 & 63 & 50 & \\     
\end{bmatrix}
$$

**$$B_{16x32}:$$**

$$
\begin{bmatrix}
 15 & 21 & 18 & 23 & 30 & 30 & 30 & 30 & 30 & 27 & 27 & 27 & 27 & 30 & 30 & 31 & 31 & 33 & 30 & 30 & 30 & 29 & 30 & 30 & 34 & 36 & 36 & 33 & 27 & 27 & 28 & 17 & \\     
 23 & 125 & 79 & 81 & 176 & 178 & 179 & 178 & 177 & 180 & 181 & 180 & 181 & 180 & 181 & 183 & 187 & 202 & 213 & 211 & 211 & 211 & 212 & 213 & 214 & 214 & 209 & 183 & 179 & 179 & 124 & 22 & \\
 31 & 141 & 86 & 89 & 199 & 210 & 208 & 211 & 207 & 207 & 208 & 211 & 214 & 215 & 221 & 224 & 230 & 227 & 226 & 234 & 234 & 241 & 239 & 234 & 235 & 237 & 229 & 222 & 205 & 208 & 141 & 22 & \\
 31 & 139 & 85 & 79 & 197 & 210 & 210 & 218 & 220 & 220 & 216 & 216 & 216 & 217 & 227 & 235 & 229 & 226 & 220 & 210 & 217 & 228 & 234 & 228 & 227 & 217 & 224 & 214 & 202 & 206 & 149 & 28 & \\
 28 & 136 & 93 & 80 & 201 & 212 & 214 & 213 & 214 & 216 & 221 & 220 & 219 & 222 & 224 & 228 & 231 & 227 & 150 & 44 & 75 & 157 & 196 & 128 & 108 & 104 & 226 & 220 & 209 & 206 & 149 & 25 & \\
 25 & 138 & 87 & 84 & 203 & 213 & 214 & 214 & 215 & 215 & 214 & 217 & 223 & 225 & 227 & 230 & 230 & 214 & 61 & 68 & 59 & 101 & 87 & 85 & 89 & 195 & 234 & 223 & 208 & 206 & 156 & 25 & \\
 29 & 136 & 80 & 72 & 200 & 210 & 209 & 210 & 208 & 205 & 209 & 217 & 222 & 219 & 220 & 228 & 230 & 206 & 59 & 27 & 51 & 124 & 80 & 25 & 59 & 206 & 231 & 210 & 208 & 204 & 167 & 27 & \\
 29 & 135 & 77 & 61 & 198 & 214 & 209 & 211 & 209 & 207 & 215 & 217 & 229 & 214 & 170 & 188 & 200 & 169 & 70 & 25 & 20 & 79 & 58 & 18 & 27 & 110 & 217 & 183 & 200 & 204 & 161 & 29 & \\
 26 & 140 & 79 & 80 & 200 & 210 & 203 & 212 & 214 & 210 & 217 & 219 & 221 & 225 & 221 & 221 & 197 & 179 & 125 & 88 & 113 & 27 & 31 & 152 & 75 & 86 & 179 & 211 & 196 & 203 & 151 & 28 & \\
 26 & 143 & 84 & 69 & 183 & 193 & 198 & 203 & 202 & 194 & 193 & 206 & 218 & 217 & 222 & 217 & 213 & 208 & 156 & 85 & 53 & 2 & 0 & 37 & 87 & 165 & 186 & 219 & 194 & 202 & 143 & 23 & \\
 26 & 137 & 75 & 70 & 190 & 201 & 199 & 187 & 140 & 108 & 113 & 109 & 173 & 159 & 147 & 189 & 185 & 172 & 171 & 97 & 5 & 7 & 9 & 2 & 68 & 92 & 177 & 204 & 191 & 195 & 142 & 23 & \\
 27 & 117 & 66 & 70 & 152 & 141 & 162 & 119 & 64 & 41 & 153 & 85 & 70 & 53 & 46 & 96 & 114 & 117 & 103 & 110 & 44 & 123 & 150 & 45 & 61 & 97 & 181 & 187 & 193 & 194 & 139 & 23 & \\
 27 & 113 & 67 & 51 & 158 & 182 & 175 & 73 & 74 & 115 & 90 & 75 & 99 & 164 & 170 & 172 & 185 & 178 & 172 & 176 & 190 & 163 & 187 & 201 & 199 & 176 & 184 & 195 & 198 & 188 & 125 & 22 & \\
 26 & 117 & 128 & 135 & 133 & 135 & 137 & 129 & 130 & 131 & 123 & 118 & 130 & 142 & 125 & 122 & 127 & 122 & 128 & 128 & 132 & 128 & 139 & 137 & 150 & 138 & 129 & 137 & 137 & 132 & 124 & 26 & \\
 26 & 120 & 130 & 122 & 109 & 119 & 123 & 110 & 115 & 133 & 122 & 115 & 107 & 112 & 117 & 101 & 119 & 100 & 111 & 112 & 112 & 118 & 125 & 114 & 122 & 116 & 124 & 124 & 126 & 119 & 114 & 27 & \\
 16 & 21 & 22 & 25 & 24 & 26 & 27 & 24 & 25 & 24 & 22 & 22 & 21 & 25 & 27 & 25 & 27 & 25 & 23 & 22 & 22 & 23 & 23 & 23 & 27 & 28 & 30 & 29 & 24 & 23 & 28 & 17 & \\     
\end{bmatrix}
$$

<br>

<div style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/RGB_channels_plot.png?raw=true"/> 

<em><b>Figura 3:</b> Plot das matrizes R, G e B juntos e separados.</em>
</div>


# 1 - Visão Computacional com Aprendizado de Máquina
A Visão Computacional é um campo da Inteligência Artificial que permite que computadores **aprendam** a interpretar e analisar imagens e vídeos, simulando a percepção visual humana. Utilizando técnicas como processamento de imagens, aprendizado de máquina e redes neurais, a visão computacional pode reconhecer objetos, detectar padrões e extrair informações visuais.

<div style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Fig4.png?raw=true"/> 

<em><b>Figura 4:</b> Rede Neural.</em>
</div>

<div style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Fig5.png?raw=true"/> 

<em><b>Figura 5:</b> Exemplo de Dataset.</em>
</div>

# 2 - Coco dataset
O [COCO Dataset](https://cocodataset.org/#home) (_Common Objects in Context_) foi criado para avançar o reconhecimento de objetos no contexto da compreensão de cenas. Ele contém imagens de cenas do dia a dia, onde os objetos aparecem em seus ambientes naturais, e são rotulados com segmentações por instância para localização precisa. O conjunto de dados inclui 91 tipos de objetos reconhecíveis por crianças de 4 anos, com um total de 2,5 M de instâncias rotuladas em **328 K imagens**. Seu desenvolvimento envolveu trabalhadores crowdsourcing e interfaces inovadoras para detecção e segmentação. 

<div style="display: inline_block" align="center">
<img hrep = "https://cocodataset.org/#home" height="400cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/coco_dataset.png?raw=true"/> 

<em><b>Figura 6:</b> Coco Dataset. [<a href="#2-coco-ref">2</a>]</em>

</div>

## 2.1 - Treinar com seu próprio Dataset

[![Assista ao vídeo](https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Thumbnail%20V%C3%ADdeo%20Como%20rotular%20dataset%20de%20detec%C3%A7%C3%A3o%20no%20roboflow.png?raw=true)](https://youtu.be/Zep7m4wSAZU?si=ebkC5gj1Nd2IcSPr)
<div style="display: inline_block" align="center">
<em><b>Vídeo 1:</b> Como rotular dataset de detecção no Roboflow. [<a href="roboflow-ref">3</a>]</em>
</div>

# <p> 3 - Diferença entre Classificação, Classificação com Localização, Detecção (e Segmentação) [<a href="#cnn-ref">4</a>]</p>


<div style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Fig7.png?raw=true"/> 

<em><b>Figura 7:</b> Clasicação vs Classificação com Localização vs Deteccção. </em>
</div>

<div style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Fig9.png?raw=true"/> 

<em><b>Figura 8:</b> Segmentação. </em>


</div>

# 4 - O que é o YOLO?

<p>O YOLO (You Only Look Once) é um modelo de detecção de objetos e segmentação de imagens em tempo real, baseado em aprendizado profundo. Ele processa a imagem inteira de uma vez, tornando a detecção mais rápida e eficiente. A versão mais recente, YOLO11 [<a href="yolo11-ref">5</a>], desenvolvida pela Ultralytics, combina avanços em velocidade e precisão, sendo altamente adaptável para diversas plataformas, desde dispositivos embarcados até aplicações em nuvem.</p>

<div style="display: inline_block" align="center">
<img height="180" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/video_seg_part1.gif?raw=true"/> 
<img height="180''" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/video_seg_part2.gif?raw=true"/> 
<img height="180" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/video_seg_part3.gif?raw=true"/>  
<em><b>Vídeo 2:</b> GIFs mostrando o YOLO em funcionamento (<a href="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/video/output.mp4">Vídeo original em melhor qualidade</a>)</em>
</div>


<video src="./results/old_episodes/simulation.mp4" controls preload></video>

## 4.1 - _Output_


<div id="fig9" style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Fig8.png?raw=true"/> 

<em><b>Figura 9:</b> Output simplificado da detecção. </em>

</div>

## 4.2 - _Sliding Window_

O algoritmo de _Sliding Windows_ é uma técnica utilizada para detectar objetos em uma imagem ao dividir a entrada em múltiplas janelas deslizantes, processando cada uma separadamente através de uma rede neural. No entanto, essa abordagem tradicional é computacionalmente cara, pois exige várias passagens pelo modelo. Para otimizar esse processo, é possível converter as camadas totalmente conectadas (_fully connected layers_) da rede em camadas **convolucionais**, permitindo que toda a imagem seja processada simultaneamente em uma única passagem, compartilhando cálculos redundantes. Essa implementação **convolucional** de _Sliding Windows_ melhora a eficiência da detecção, tornando-a significativamente mais rápida, mas ainda apresenta desafios na precisão da localização das caixas delimitadoras (_bounding boxes_), o que pode ser refinado em etapas posteriores do modelo.

<div style="display: inline_block" align="center">
<img height="250" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/sliding_window1.gif?raw=true"/> 
<img height="250''" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/sliding_window2.gif?raw=true"/> 
<img height="250" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/sliding_window3.gif?raw=true"/>  
 
<em><b>Vídeo 3:</b> Sliding Window.</em>
</div>

## 4.3 - _Nonmax Suppression_
_Nonmax Suppression_ (NMS) é um método usado na detecção de objetos para remover previsões redundantes e garantir que cada objeto seja identificado apenas uma vez. Para isso, utiliza-se a métrica _Intersection over Union_ (IoU), que mede a sobreposição entre a caixa predita e a real. O algoritmo ordena as previsões por nível de confiança, seleciona a de maior probabilidade e descarta as demais que possuam alta sobreposição. Esse processo reduz falsos positivos e melhora a precisão do modelo.

<div style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Fig10.png?raw=true"/> 

<em><b>Figura 10:</b> Nonmax Suppression. </em>

</div>

## 4.4 - _Ancher boxes_

A técnica de *Anchor Boxes* permite que um único *grid cell* detecte múltiplos objetos ao associá-los a caixas predefinidas de diferentes formatos. Cada objeto é atribuído à *anchor box* que apresenta maior *Intersection over Union* (IoU) com seu *bounding box* real. Dessa forma, a rede pode detectar simultaneamente objetos de diferentes proporções em uma mesma célula, evitando conflitos quando múltiplos objetos compartilham a mesma região. Além disso, *anchor boxes* possibilitam uma especialização mais eficiente do modelo, permitindo que diferentes unidades se ajustem a objetos de formas variadas, como gatos e bolas de esporte.

<div style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Fig11.png?raw=true"/> 

<em><b>Figura 11:</b> Anchor boxes. </em>
</div>

<p>Assim como na <a href="#fig9">Figura 9</a>, o <I>Output</I> (ŷ) retorna os mesmos dados da <I>Bounding box</I>. Contudo, ele vai retornar esses dados para cada Bounding box como mostrado no exemplo da <a href="#fig12">Figura 12</a>.</p>

Modelos de detecção mais eficientes podem dividir as imagens em muito mais células, possuir dezenas de *Ancher boxes* diferentes e possuir centenas de classes de objetos.

<div id="fig12" style="display: inline_block" align="center">
<img height="600cm" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Fig12.png?raw=true"/> 

<em><b>Figura 12:</b> Exemplo de output com mais de uma Anchor boxes. </em>

</div>

## 4.5 - _Region Proposals (R-CNN)_

<p>A <I>R-CNN</I> [<a href="#rcnn-ref">6</a>] (<I>Regions with Convolutional Neural Networks</I>) é um modelo de detecção de objetos que utiliza <I>Region Proposals</I> para reduzir o número de regiões analisadas. Primeiro, um algoritmo de segmentação identifica áreas de interesse, e, em seguida, uma rede neural convolucional classifica cada região proposta e refina a localização dos objetos. Embora apresente bons resultados, a <I>R-CNN</I> é lenta, pois processa cada região separadamente, tornando a inferência computacionalmente cara.</p>

<div id="fig12" style="display: inline_block" align="center">
<img height="400" src="https://media.geeksforgeeks.org/wp-content/uploads/20200219133430/seelctive-search.png"/> 

<em><b>Figura 12:</b> Region Proposals. [<a href="#r-cnn-geeksforgeeks-ref">7</a>]</em>

</div>

Resumo: Propor regiões. Classificar as regiões propostas uma de cada vez. Retornar rótulo + caixa delimitadora.

## 4.6 - _Fast R-CNN_
<p>O Fast R-CNN [<a href="#girshick2015-fastrcnn-ref">8</a>] Otimiza o processo de detecção de objetos ao substituir a abordagem tradicional de classificação de regiões individuais. Em vez de classificar cada região proposta separadamente, ele utiliza uma implementação convolucional de <I>sliding windows</I> para processar todas as regiões propostas simultaneamente. Isso reduz significativamente o tempo de inferência ao compartilhar computação entre as regiões, mantendo a precisão na classificação e na delimitação dos objetos detectados.</p>

## 4.7 - _Faster R-CNN_
<p>Faster R-CNN [<a href="#ren2016-fasterrcnn-ref">9</a>] aprimora o processo de detecção de objetos ao substituir algoritmos tradicionais de proposta de regiões por uma <I>Rede Neural Convolucional</I> (<I>CNN</I>). Essa abordagem permite que as regiões candidatas sejam geradas diretamente pela rede, reduzindo significativamente o tempo de processamento em comparação com métodos anteriores, como <I>R-CNN</I> e <I>Fast R-CNN</I>.</p>

# 5 - Principais Tarefas do YOLO
YOLO11 é uma estrutura de IA que suporta múltiplas tarefas de visão computacional. A estrutura pode ser utilizada para efetuar a deteção, segmentação, obb, classificação e estimativa de pose. Cada uma destas tarefas tem um objetivo e um caso de utilização diferentes.

<div id="fig12" style="display: inline_block" align="center">
<img height="200" src="https://github.com/ultralytics/docs/releases/download/0/ultralytics-yolov8-tasks-banner.avif"/> 

<em><b>Figura 12:</b> Tarefas suportadas pelo modelo YOLOv11 da Ultralytics. [<a href="#yolo11-ref">5</a>]</em>

</div>

# 6 - Aplicações de YOLO na LUNAR (começo de 2025)

<div style="display: inline_block" align="center">
<img height="250" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/post_processing_Video_for_test1.gif?raw=true"/> 
<img height="250" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/post_processing_Video_for_test2.gif?raw=true"/> 
 
<em><b>Vídeo 3:</b> Deteccção de Cones treinada pela LUNAR.</em>
</div>

# 7 - Outras aplicações do YOLO
## 7.1 - Automóveis 

<div style="display: inline_block" align="center">
<img height="250" src="https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/22606/images/8f2826-80f-051b-177b-5ff744de085c_ezgif.com-gif-maker_2_.gif"/> 
 
<img height="250" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/car1.gif?raw=true"/> 

<em><b>Vídeo 4:</b> Uso de Visão Computacional aplicado para veículos autônomos. [<a href="#Rebeca">11</a>]</em>

</div>

## 7.2 - Esportes e Entretenimento

<div style="display: inline_block" align="center">
<img height="400" src="https://github.com/LUNAR-ICTS/-Seminarios/blob/main/Marco%202025/YOLO/assets/img/Rebeca_poses_medium.gif?raw=true"/> 

<em><b>Vídeo 5:</b> YOLOv11 Poses aplicado no vídeo da Rebeca Andrade. [<a href="#Rebeca">11</a>]</em>

</div>

## 7.3 - Indústria 
## 7.4 - Ambiental
## 7.5 - Agro
## 7.6 - Saúde
## 7.7 - Civil
## 7.8 - Acessibilidade
## 7.9 - Segurança e Estética
# 8 - Principal Concorrente do YOLO
# 9 - Referências
<h4 id="1-mojang-ref">[1] Mojang Studios, "Mojang Studios Official Website," [Online]. Available: <a href="https://www.minecraft.net/">https://www.minecraft.net/</a>. Accessed: 2025-03-06.</h4>

<h4 id="2-coco-ref">[2] T.-Y. Lin, M. Maire, S. Belongie, L. Bourdev, R. Girshick, J. Hays, P. Perona, D. Ramanan, C. L. Zitnick, and P. Dollár, "Microsoft COCO: Common Objects in Context," <em>arXiv preprint arXiv:1405.0312</em>, 2015. [Online]. Available: <a href="https://arxiv.org/abs/1405.0312">https://arxiv.org/abs/1405.0312</a></h4>

<h4 id="roboflow-ref">[3] LUNAR - ICTS, "Como rotular dataset de detecção no Roboflow," [Online]. Available: <a href="https://www.youtube.com/watch?v=Zep7m4wSAZU">https://www.youtube.com/watch?v=Zep7m4wSAZU</a>. Accessed: 2025-03-06.</h4>

<h4 id="cnn-ref">[4] A. Ng, "Convolutional Neural Networks," DeepLearning.AI, 2017. [Online]. Available: 
<a href="https://www.coursera.org/learn/convolutional-neural-networks">https://www.coursera.org/learn/convolutional-neural-networks</a>. 
Available: <a href="https://www.youtube.com/playlist?list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF">https://www.youtube.com/playlist?list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF</a>. 
Accessed: 2025-03-06.</h4>

<h4 id="yolo11-ref">[5] Glenn Jocher and Jing Qiu, "Ultralytics YOLO11," version 11.0.0, 2024. [Online]. Available: <a href="https://github.com/ultralytics/ultralytics">https://github.com/ultralytics/ultralytics</a>. License: AGPL-3.0. ORCID: 0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069. Accessed: 2025-03-06.</h4>

<h4 id="rcnn-ref">[6] Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra Malik, "Rich feature hierarchies for accurate object detection and semantic segmentation," 2014. [Online]. Available: <a href="https://arxiv.org/abs/1311.2524">https://arxiv.org/abs/1311.2524</a>. Accessed: 2025-03-06.</h4>

<h4 id="r-cnn-geeksforgeeks-ref">[7] GeeksforGeeks, "R-CNN – Region-Based Convolutional Neural Networks," [Online]. Available: <a href="https://www.geeksforgeeks.org/r-cnn-region-based-cnns/">https://www.geeksforgeeks.org/r-cnn-region-based-cnns/</a>. Accessed: 2025-03-07.</h4>

<h4 id="girshick2015-fastrcnn-ref">[8] Ross Girshick, "Fast R-CNN," 2015. [Online]. Available: <a href="https://arxiv.org/abs/1504.08083">https://arxiv.org/abs/1504.08083</a>. Accessed: 2025-03-07.

<h4 id="ren2016-fasterrcnn-ref">[9] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun, "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks," 2016. [Online]. Available: <a href="https://arxiv.org/abs/1506.01497">https://arxiv.org/abs/1506.01497</a>. Accessed: 2025-03-07.</h4>
<h4 id="Car_vision">[10] </h4>

<h4 id="Rebeca">[11] Olympics Gymnastics, "Rebeca Andrade's GOLD 🥇✨medal floor routine | Music Monday," YouTube, Sep. 9, 2024. [Online]. Available: <a href="https://www.youtube.com/watch?v=xXKM8ThtYOE">https://www.youtube.com/watch?v=xXKM8ThtYOE</a>. Accessed: Mar. 7, 2025.</h4>


