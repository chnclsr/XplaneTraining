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
