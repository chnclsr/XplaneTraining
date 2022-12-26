# B_X-Plane 11
Bu çalışma X-Plane 11 uçuş simülasyonu üzerinde sanal varlıkların pekiştirmeli öğrenme ile eğitilebilmesi için
gerekli gym ortamı ve öğrenme metotlarını içermektedir. Bir uçağın manevra kabiliyetlerinin yanısıra 
sensör ve savunma sistemlerinin de uygun görevlerde kullanımı mümkündür.

# Pekiştirmeli Öğrenme Uygulamaları
Pekiştirmeli Öğrenmede Ajan(agent), bulunduğu
ortam(enviroment) ile etkileşime geçer. Pekiştirmeli Öğrenme, Markov karar süreci model kullanmaktadır. 
Algılama (sensation), eylem (action) ve hedef (goal) Markov karar süreçlerinin en önemli 3 özelliğidir.
Her bir durum sadece ve sadece bir önceki durumun sonucudur. Ajan eylemler gerçekleştirerek farklı
durumlara geçiş yapar. Ajanın amacı aldığı ödül miktarını arttırmaktır. Belirli bir ödül-ceza sistemine
göre eğitilen ajan zamanla en fazla ödülü alabileceği taktiği keşfederek görevi gerçekleştirmeyi öğrenir.



![Pekiştirmeli Öğrenme Kavramları Etkileşim Diyagramı](/readmeimg/S3-4-1.png)
Şekil 3.4.1 Pekiştirmeli Öğrenme Kavramları Etkileşim Diyagramı [8]
Bu projede iki ayrı Pekiştirmeli Öğrenme algoritmasının uygulaması gerçekleştirilmiştir.
Bunlar; Yakınsal Poliçe Optimizasyon Algoritmaları (Proximal Policy Optimization
Algorithms)(PPO) ve Derin Pekiştirmeli Q-Öğrenme(Deep Q-Learning)

# Oyun Tasarımı
Oyunu tasarlarken ana karakterin olması önündeki engellere atış yapabileceği ve bu
engellerin karaktere çarpması durumunda ana karakterin oyunu kaybetmesi ile oyunun
sonlanması planlanmıştır. Engellerin ise rastgele bir şekilde ana karaktere doğru
ilerleyerek hareket etmeleri hedeflenmiştir. Ana karakterin davranış seçenekleri
arasında yer değiştirmek ve engellere atış yapmak vardır.
Oyunun hikayesi ise bir Kedinin önüne çıkan balıklara karşı kendini koruması ve onları
gerekirse avlaması gerektiği. Projenin en son karar kılınan hikayesi bu şekildedir.

![Catastrophe](/readmeimg/S1-1-1.png "screenshot of the game")

# Oyunu oynamak ve Pekiştirmeli Öğrenme ile eğitmek 

Kurulum için miniconda kullanılması tavsiye edilir.Ama zorunlu değildir 
miniconda kurulumu için linkten kullandığınız işletim sistemine uygun sürümü seçiniz ve kurunuz 

[MiniConda Latest Install](https://docs.conda.io/en/latest/miniconda.html)

## Eğer Miniconda kullanarak çalıştıracaksanız ilk 3 adımı uygulayınız: 

#### MiniConda kurulumundan sonra conda alanını oluşturunuz
```
conda create --name test1 
```

#### Oluşturduğunuz alanı aktive ediniz 
```
conda activate test1
```

#### Conda üzerinde GYM modülünü yükleyin Eğer Conda ile kuruluma devam etmiyorsanız pip ile yükleyiniz 
```
conda install -c conda-forge gym-all
pip install gym-all
```


### Stable-Baselines3'ü yükleyiniz 
```
pip install stable-baselines3[extra] 
```

### Pyglet'i yükleyiniz 
```
pip install pyglet 
```

### Tensorflow'u yükleyiniz 
```
pip install tensorflow
```

### Tensorflow-gpu yükleyiniz
```
pip install tensorflow-gpu
```

### Pygame'i yükleyiniz
```
pip install pygame 
``` 
