**Aplicação de Tecnologias na Personalização de Experiências Multissensoriais: Uma Abordagem para a harmonização entre Música e Bebidas**

**Júlia Zanin Monteiro1**

1Faculdade de Computação e Informática (FCI)  
Universidade Presbiteriana Mackenzie – São Paulo, SP – Brasil

{10400678}@mackenzista.com.br

**Resumo.** Este trabalho apresenta o desenvolvimento do Drunkify, um aplicativo interativo que visa proporcionar experiências sensoriais personalizadas ao unir bebidas alcoólicas, música, memórias afetivas e tecnologias emergentes, como inteligência artificial (IA), Machine Learning (ML) e realidade aumentada (RA). A proposta parte da observação de que músicas específicas têm o poder de recordar lembranças, influenciar o comportamento do consumidor e promover conexões emocionais com produtos e momentos. O Drunkify permite que usuários personalizem drinks com base em estilos musicais, humores e playlists, além de vivenciarem experiências multissensoriais ao escanear bebidas e visualizar animações em RA que contam a história da bebida, acompanhadas de sugestões musicais. O aplicativo também integra gamificação, desafios de mixologia, parcerias com bares e eventos, além de explorar modelos de monetização por meio de e-commerce de kits exclusivos e assinaturas. A metodologia envolve pesquisa bibliográfica sobre música, memória, comportamento do consumidor e tecnologias imersivas, além do desenvolvimento de uma interface amigável e responsiva. Como resultado, o projeto propõe uma nova forma de interação afetiva com o consumo, transformando momentos cotidianos em experiências marcantes, contribuindo para as áreas de marketing sensorial, experiência do usuário (UX) e inovação tecnológica no consumo emocional.

**Palavras-chave:** Percepção sensorial; música e emoções; bebidas; realidade aumentada; comportamento do consumidor; experiência personalizada.

***Abstract.** This work presents the development of Drunkify, an interactive application designed to provide personalized sensory experiences by combining alcoholic beverages, music, emotional memories, and emerging technologies such as Artificial Intelligence (AI), Machine Learning (ML), and Augmented Reality (AR). The proposal stems from the observation that specific songs have the power to recall memories, influence consumer behavior, and create emotional connections with products and moments. Drunkify enables users to customize drinks based on musical styles, moods, and playlists, while also offering multisensory experiences by scanning beverages and visualizing AR animations that tell the story behind the drink, accompanied by musical suggestions. The app also features gamification elements, mixology challenges, partnerships with bars and events, and explores monetization models through exclusive e-commerce kits and subscriptions. The methodology involves bibliographic research on music, memory, consumer behavior, and immersive technologies, along with the development of a user-friendly and responsive interface. As a result, the project proposes a new form of emotional interaction with consumption, turning everyday moments into memorable experiences and contributing to the fields of sensory marketing, user experience (UX), and technological innovation in emotional consumption.*

***Keywords:** Sensory experience; music and emotions; beverages; augmented reality; consumer behavior; customized experience.*

**1\. Introdução**

O avanço das tecnologias digitais têm transformado a forma como as pessoas interagem com produtos, serviços e experiências. Com a popularização de dispositivos móveis, aplicativos interativos e soluções baseadas em inteligência artificial (IA), tornou-se possível oferecer experiências cada vez mais personalizadas, imersivas e envolventes. Nessa dinâmica, os sentidos, as emoções e as memórias passam a desempenhar um papel fundamental, criando conexões afetivas entre usuários e o que eles consomem.

O Drunkify, um aplicativo interativo que combina bebidas, música e algoritmos de IA e Machine Learning (ML), está sendo criado para proporcionar experiências únicas e personalizadas. Ao considerar o humor e o estilo musical do usuário, o aplicativo irá sugerir combinações de bebidas e desafios interativos que despertem emoções e memórias, tornando a experiência mais divertida e memorável.

O desafio central deste projeto é entender como a tecnologia pode ajudar a personalizar experiências sensoriais, criando recomendações inteligentes que façam sentido para cada usuário. Observou-se que, apesar do crescente uso de aplicativos interativos, ainda há poucas soluções que integrem de forma inteligente música, sabores e estímulos visuais para oferecer experiências personalizadas e lúdicas. O Drunkify busca preencher essa lacuna, usando IA para relacionar preferências, humor e música, e entregar sugestões de forma prática e envolvente.

O objetivo geral deste trabalho é desenvolver um aplicativo capaz de proporcionar experiências sensoriais diferenciadas, combinando música, bebidas e recomendações inteligentes baseadas em IA. Entre os objetivos específicos estão:

* utilizar um dataset real de características musicais relacionadas com emoções;  
* explorar como elementos de gamificação e interatividade podem tornar a experiência mais divertida;  
* demonstrar como a IA pode ser aplicada em aplicativos de entretenimento digital.

Este estudo é relevante porque mostra como a tecnologia pode transformar o consumo em algo mais significativo e afetivo, criando experiências únicas e memoráveis. O Drunkify conecta usuários, música e bebidas de maneira criativa, se juntando às tendências de personalização e experiência digital.

**2\. Problema e Aspectos Éticos da IA**

Hoje em dia, as pessoas buscam experiências mais personalizadas e significativas, que vão além de simplesmente consumir produtos ou serviços. Apesar de existirem aplicativos de entretenimento e plataformas de recomendação, ainda são raras as soluções que consigam unir diferentes estímulos sensoriais, como música, bebidas e elementos visuais, criando uma experiência completa e envolvente.

O Drunkify foi pensado para preencher essa lacuna. O aplicativo combina humor, estilo musical e recomendação de bebidas usando inteligência artificial (IA) e Machine Learning (ML), para criar experiências divertidas, memoráveis e personalizadas. O desafio é fazer com que a IA sugira bebidas e músicas que realmente combinem com o humor do usuário, tornando a experiência divertida, segura e envolvente.

Além disso, é importante considerar os aspectos éticos:

* Transparência: o usuário sabe que as recomendações vêm de algoritmos e servem para personalização e diversão.  
* Uso responsável: o foco está na experiência sensorial e na diversão, sem incentivar o consumo excessivo de álcool.  
* Equidade: o modelo deve ser justo, sem favorecer ou prejudicar qualquer grupo de usuários.  
* Responsabilidade: o projeto é um estudo de caso que mostra como usar IA e gamificação de forma segura e ética.

Com essa abordagem, o Drunkify consegue criar experiências divertidas, personalizadas e seguras, integrando música, bebidas e interatividade de forma natural e envolvente.

### **4\. Opção do Projeto**

Este trabalho foi desenvolvido de acordo com a Opção Framework, que exige o uso de ferramentas de Machine Learning/Deep Learning para resolver problemas de análise ou recomendação de dados.

Foi utilizada uma base de dados real, contendo informações sobre humor e  estilos musicais, com o objetivo de simular cenários reais de uso. Esses dados foram processados e analisados em Python, utilizando bibliotecas como pandas, matplotlib, seaborn e scikit-learn.

Essa abordagem permitiu aplicar técnicas de pré-processamento, análise exploratória e modelagem simples, com o objetivo de demonstrar a viabilidade de um sistema de recomendação personalizado. 

**4\. Data Set**

Para o protótipo do Drunkify, foi utilizado um dataset real sobre dados do *Spotify* para identificar humores com o objetivo de simular o perfil de usuários, seus humores, estilos musicais preferidos e preferências de bebidas.

O dataset contém as seguintes informações:

* **name** \- Nome da música  
* **album** \- Nome do álbum  
* **artist** \- Nome do artista  
* **id** \- ID único da música no Spotify  
* **release\_date** \- Data de lançamento  
* **popularity** \- Popularidade (0-100)  
* **length** \- Duração da música (milissegundos)  
* **danceability** \- Dançabilidade (0-1)  
* **acousticness** \- Natureza acústica (0-1)  
* **energy** \- Energia (0-1)

4.1 Análise Exploratória

A análise exploratória teve como objetivo compreender as características musicais objetivas presentes no dataset e identificar padrões que pudessem orientar os mapeamentos de humor e as recomendações automatizadas do sistema. Utilizou-se o dataset público "Spotify Music Data to Identify Moods" (Kaggle), contendo 686 músicas com features de áudio validadas pela API do Spotify.

Foram analisadas distribuições de *energy* (energia), *danceability* (dançabilidade) e *acousticness* (natureza acústica), identificando padrões que orientaram os mapeamentos de humor e recomendações automatizadas. Observou-se, por exemplo, que músicas com alta *energy* e danceability associam-se ao humor "animado", enquanto baixa *energy* relaciona-se a "relaxado" ou "cansado".

4.2 Preparação dos Dados

Para que os dados pudessem ser utilizados em algoritmos de Machine Learning, foi necessário realizar algumas transformações:

* Mapeamento de variáveis;  
* Conversão de categorias em números: usando LabelEncoder, transformando campos como humor, estilo musical e bebida favorita em valores numéricos;  
* Normalização de features: aplicação de StandardScaler nas features numéricas (energy, danceability, acousticness) para garantir que todas as variáveis contribuam igualmente no modelo;  
* Verificação de valores ausentes: não foram identificados casos incompletos no dataset original do Spotify;

O dataset ficou pronto para aplicação de modelos simples de classificação, permitindo simular recomendações de bebidas e músicas personalizadas de acordo com o humor e preferências do usuário.

**5\. Metodologia**

Esta pesquisa classifica-se como aplicada, de abordagem qualitativa, com delineamento exploratório e descritivo. O caráter aplicado justifica-se pela busca de uma solução prática para criar experiências personalizadas de entretenimento, utilizando bebidas, música e tecnologias digitais, especialmente inteligência artificial (IA) e Machine Learning (ML). A abordagem qualitativa é adequada para investigar fenômenos subjetivos, como preferências de humor e estilo musical, e analisar como estas escolhas podem influenciar recomendações personalizadas. O delineamento exploratório reflete a natureza inovadora do projeto, uma vez que não existem, até o momento, plataformas que integrem IA, gamificação e experiências sensoriais de forma coordenada nesse contexto. A dimensão descritiva está presente na documentação detalhada do processo de criação do protótipo, permitindo registrar o percurso metodológico adotado.

A primeira etapa da pesquisa consistiu em uma revisão bibliográfica com o objetivo de estudar a personalização e recomendação por IA, a gamificação e o engajamento do usuário, além de experiências sensoriais mediadas por tecnologia.

Na etapa seguinte, foi conduzida uma análise exploratória de soluções tecnológicas existentes, como aplicativos de recomendação de bebidas, plataformas de música interativa e iniciativas que aplicam IA e gamificação em entretenimento digital. 

**6\. Resultados**

O projeto utilizou o dataset público "Spotify Music Data to Identify Moods" (Kaggle), contendo 686 músicas do período de 1966-2020, com features de áudio validadas pela API do Spotify. Após o processamento, foram identificados 7 humores distintos e mapeadas categorias de bebidas baseadas em características musicais.

6.1 Análise Exploratória

A análise revelou padrões consistentes entre características musicais e humores:

* Músicas com alta *energy* e *danceability* associaram-se ao humor "animado"  
* Baixa energy correlacionou-se com "relaxado" e "cansado"  
* Alta *acousticness* relacionou-se a humores contemplativos

As relações humor-bebida mapeadas com base em Carvalho et al. (2016) e Jacob (2006) mostraram coerência: humores positivos relacionaram-se a bebidas sociais (cerveja, espumante), enquanto humores contemplativos associaram-se a bebidas de apreciação (vinho, whisky).

6.2 Modelo de Machine Learning

Foram treinados dois algoritmos de classificação (Decision Tree e Random Forest) para recomendar bebidas com base em humor e características musicais. O Random Forest apresentou melhor desempenho e foi selecionado como modelo final.

Configuração:

* Features utilizadas: humor, estilo musical, energy, danceability, acousticness (normalizadas)  
* Target: categoria de bebida  
* Divisão: 80% treino (549 amostras) / 20% teste (137 amostras)  
* Validação: Cross-validation 5-fold

A análise de importância das features revelou que humor e características musicais contribuem de forma equilibrada para as recomendações, validando a abordagem de integrar múltiplas dimensões sensoriais.

6.3 Validação e Consistência

O modelo demonstrou consistência com a fundamentação teórica: recomendações para humores positivos alinharam-se com bebidas sociais (Jacob, 2006), e a relação entre energia musical e intensidade de bebida mostrou-se coerente com Carvalho et al. (2016).

Artefatos gerados: dataset processado, modelos treinados com encoders, visualizações em alta resolução, documentação completa e código reprodutível.

Limitações observadas: tamanho moderado do dataset (686 músicas), mapeamentos baseados em literatura, e viés cultural . Estas limitações são reconhecidas e discutidas, mas não comprometem a validade da prova de conceito desenvolvida.

**7\. Conclusões**

O projeto Drunkify teve como objetivo criar um sistema de recomendação que unisse música, emoções e bebidas de forma personalizada, usando inteligência artificial. A ideia foi mostrar que é possível gerar experiências sensoriais únicas com base em dados reais e ciência, conectando as características de músicas, o humor das pessoas e suas preferências de consumo. Para isso, foi utilizado um conjunto de dados real do Spotify com 686 músicas e suas métricas validadas, além de uma base teórica em estudos sobre música, emoções e comportamento humano.

Os resultados foram muito positivos. O projeto conseguiu utilizar um dataset real e confiável, mapeou humores a partir de características musicais e estabeleceu relações entre emoções e tipos de bebidas baseadas em pesquisas científicas. O modelo de Machine Learning (Random Forest) funcionou bem e mostrou que essa integração é viável tecnicamente. 

Mesmo com esses avanços, algumas limitações foram reconhecidas. O conjunto de músicas, embora adequado para o teste, ainda é pequeno para uma aplicação ampla, não houve uma validação prática com pessoas para medir a satisfação com as recomendações, e também, o dataset é predominantemente ocidental, o que pode limitar a diversidade cultural.

O trabalho mostrou como é possível unir teoria científica e dados reais em projetos de IA aplicada, promoveu uma integração entre áreas muito diferentes, como psicologia, música e tecnologia, e reforçou a importância da ética em projetos.

Futuramente, o projeto pode evoluir em várias direções. Em um primeiro momento, seria interessante coletar dados reais de usuários, testar o sistema com pessoas e aumentar a diversidade musical do dataset. Em seguida, pode-se desenvolver um protótipo funcional do Drunkify, integrando a API do Spotify para gerar recomendações em tempo real e realizando testes com usuários para medir a satisfação. Em seguida, o ideal seria realizar experimentos controlados que validem cientificamente as relações entre música, humor e bebida, além de explorar novos contextos.

O Drunkify mostrou que é possível criar experiências personalizadas e significativas usando tecnologia e ciência de forma criativa. Mesmo sendo um projeto conceitual, ele abre portas para novas formas de unir música, emoções e consumo de maneira inovadora. Ao mesmo tempo em que respeita os limites éticos e metodológicos, o projeto propõe um olhar mais humano sobre o papel da inteligência artificial, não apenas como ferramenta de automação, mas como meio de gerar conexões emocionais mais ricas entre pessoas e experiências.

**8\. Referências bibliográficas**

GOFFIN, Kris. Music feels like moods feel. Frontiers in Psychology, v. 5, 2014\. Disponível em: https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00327/full. Acesso em: 06 abr. 2025\.

CARROLL, Noël. Art and mood: preliminary notes and conjectures. Monist, v. 86, p. 521–555, 2003\. DOI: https://doi.org/10.5840/monist200386426.

CARROLL, Noël; MOORE, Margaret. Not reconciled: comments for Peter Kivy. Journal of Aesthetic and Art Criticism, v. 65, p. 318–322, 2007\. DOI: https://doi.org/10.1111/j.1540-594X.2007.00263.x.

MORGAN, J. D. Music lives on: fine tuning the memory. Disponível em: https://www-

periodicos-capes-gov-br.ez347.periodicos.capes.gov.br/index.php/acervo/buscador.html?task=detalhes\&source=all\&id=W2771330718. Acesso em: 06 abr. 2025\.

WINFREY, Oprah. Oprah interviews Stevie Wonder. Disponível em: https://www.oprah.com/omagazine/oprah-interviews-stevie-wonder/2. Acesso em: 06 abr. 2025\.

SACKS, Oliver. Musicophilia: Tales of Music and the Brain. New York: Alfred A. Knopf, 2007\. Também disponível em: https://www.amazon.com.br/dp/B00FGCC6N2. Acesso em: 06 abr. 2025\.

WANG, Qian Janice; SPENCE, Charles. Assessing the role of emotional associations in mediating crossmodal correspondences between classical music and red wine. Disponível em: [https://www-periodicos-capes-gov-](https://www-periodicos-capes-gov-) br.ez347.periodicos.capes.gov.br/index.php/acervo/buscador.html?task=detalhes\&source=all\&id=W2564738268. Acesso em: 06 abr. 2025\.

CARVALHO, Felipe Reinoso; VELASCO, Carlos; VAN EE, Raymond; LEBOEUF, Yves; SPENCE, Charles. Music influences hedonic and taste ratings in beer. Frontiers in Psychology, 2016\. Disponível em: https://www.frontiersin.org/articles/10.3389/fpsyg.2016.00636/full. Acesso em: 06 abr. 2025\.

CARVALHO, Felipe Reinoso et al. Music influences hedonic and taste ratings in beer. PubMed, 2016\. Disponível em: https://pubmed.ncbi.nlm.nih.gov/27199862/. Acesso em: 06 abr. 2025\.

JACOB, Céline. Styles of background music and consumption in a bar: An empirical evaluation. International Journal of Hospitality Management, 2006\. Disponível em: https://www.sciencedirect.com/science/article/abs/pii/S027843190600003X. Acesso em: 06 abr. 2025\.

CARVALHO, Felipe Reinoso et al. Does music influence the multisensory tasting experience? Journal of Sensory Studies, 2015\. Disponível em: https://onlinelibrary.wiley.com/doi/abs/10.1111/joss.12168. Acesso em: 06 abr. 2025\.
