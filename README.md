# B_X-Plane 11
Bu çalışma X-Plane 11 uçuş simülasyonu üzerinde sanal varlıkların pekiştirmeli öğrenme ile eğitilebilmesi için
gerekli gym ortamı ve öğrenme metotlarını içermektedir. Bir uçağın manevra kabiliyetlerinin yanısıra 
sensör ve savunma sistemlerinin de uygun görevlerde kullanımı mümkündür.

# Pekiştirmeli Öğrenme
Pekiştirmeli Öğrenmede Ajan(agent), bulunduğu
ortam(enviroment) ile etkileşime geçer. Pekiştirmeli Öğrenme, Markov karar süreci model kullanmaktadır. 
Algılama (sensation), eylem (action) ve hedef (goal) Markov karar süreçlerinin en önemli 3 özelliğidir.
Her bir durum sadece ve sadece bir önceki durumun sonucudur. Ajan eylemler gerçekleştirerek farklı
durumlara geçiş yapar. Ajanın amacı aldığı ödül miktarını arttırmaktır. Belirli bir ödül-ceza sistemine
göre eğitilen ajan zamanla en fazla ödülü alabileceği taktiği keşfederek görevi gerçekleştirmeyi öğrenir.


Bu projede üç ayrı Pekiştirmeli Öğrenme algoritmasının uygulaması gerçekleştirilmiştir.
Bunlar; Poliçe tabanlı Yakınsal Poliçe Optimizasyon Algoritması (Proximal Policy Optimization
Algorithm)(PPO), aktör kritik tabanlı Yumuşatılmış Aktör Kritik (Soft Actor Critic) ve Avantaj Fonksiyonlu Aktör Kritik 
(Advantage Actor Critic) metotlarıdır.

# X-Plane 11 Ortamı
X-Plane 11 simülasyonu ana sunucusu ile UDP üzerinden paket alışverişini desteklemektedir. 
[XPlaneConnect](https://github.com/adderbyte/GYM_XPLANE_ML/tree/master/gym_xplane_final_version)
eklentisiyle simülasyon tarafında yazılabilecek ve okunabilecek veriler temel fonksiyonlarla 
kodlanmıştır.  Çalışmada simülasyon ortamı-ajan haberleşmesi için bu yapı kullanılmaktadır. 

Eğitim için planlanan ilk görevde F-4 Phantom uçağı eğitilmektedir. Hedef olarak, rastgele roll açısı ve
hızlardaki başlangıçlarda kanatları düzeltme ve roll değerini 0-20 derece aralığında tutma beklenmektedir.
20 derece kontrolde sapma üst limitidir. Ajan alacağı aksiyonlarla roll açısını bu aralıkta tutarak uçağı
sağa sola yalpalamasını önlemeye çalışmalıdır. Ajanın eğitilebilmesi için gerekli durum değerleri ve aksiyonlar
aşağıdaki gibidir.

| Durum Değerleri |  |
|-----------------|-----------------|
| Enlem           | Roll            |
| Boylam          | Rudder          |
| Yükseklik       | Pitch           |
| x               | Düşey Hız (x)   |
| y               | Düşey Hız (y)   |
| z               | Düşey Hız (z)   |
| Throttle        |                 |

#### Aksiyonlar -1 +1 aralığında yani -180 derece ile +180 derece arasındadır. Her aksiyon -/+ 18 derecelik roll değerleridir. 

| Aksiyonlar      |                |
|-----------------|----------------|
| 21              | Ayrık aksiyon  |
| 1 > -1 x 180    | 12 > 0.1 x 180 |
| 2 > -0.9 x 180  | 13 > 0.2 x 180 |
| .. > ..         | .. > ..        |
| 10 > -0.1 x 180 | 20 > 1 x 180   |
| 11 > 0 x 180    |                |

# Ödül Fonksiyonu

x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2b} 


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
