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

#### Durum değerleri dataref sorgusu ile alınmakta, her değer kendi maksimum değerine göre normalize edilmektedir.
| Durum Değerleri | Dataref                                           |
|-----------------|---------------------------------------------------|
| Enlem           | "sim/flightmodel/position/latitude"               |
| Boylam          | "longitude": "sim/flightmodel/position/longitude" |
| Yükseklik       | "sim/flightmodel/position/elevation"              |
| x               | "sim/flightmodel/position/local_x"                |
| y               | "sim/flightmodel/position/local_y"                |
| z               | "sim/flightmodel/position/local_z"                |
| Throttle        | "sim/multiplayer/position/plane0_throttle"        |
| Roll            | "sim/multiplayer/position/plane0_the              |
| Rudder          | "sim/multiplayer/position/plane0_phi"             |
| Pitch           | "sim/multiplayer/position/plane0_psi"             |
| Düşey Hız (x)   | "sim/multiplayer/position/plane0_v_x"             |
| Düşey Hız (y)   | "sim/multiplayer/position/plane0_v_y"             |
| Düşey Hız (z)   | "sim/multiplayer/position/plane0_v_z"             |

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
#### Ödül değeri hesaplanırken roll açısının belirli bir aralıkta olması pozitif etkilerken tolerans üzerinde değer arttıkça ceza artmaktadır.
Ödül = (-1) x ((|Roll açısı| - Roll limit değeri) / (180 - Roll limit değeri))


# Gereklilikler
> CUDA 10.2 \
> Python 3.8 \
> X-Plane 11 \
> XPlaneConnect

## GYM ortamı kurulu
#### 1. X-Plane ML [reposundaki](https://github.com/adderbyte/GYM_XPLANE_ML/tree/master/gym_xplane_final_version), “Installation guide” kısmındaki adımları ilk ve son adım harici uygulayın. (REPO dosyalarını değil, 2. Adımdaki dosyaları kullanın!!)
#### 2. GYM ortamını kurun.
```
pip install --upgrade pip
pip install -e .
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
