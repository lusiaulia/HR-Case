# Proyek Akhir: Menyelesaikan Permasalahan Human Resource Attrition pada Perusahaan Jaya Jaya Maju 

## Business Understanding
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Permasalahan Bisnis

- Dari data data mengenai karyawan seperti umur, divisi, pendidikan, dll yang dimiliki oleh perusahaan Jaya Jaya Maju, data mana sajakah yang berpengaruh besar terhadap attrition rate?

### Cakupan Proyek

- Pengaksesan Data:  memastikan data yang sudah disediakan oleh perusahaan dapat diakses
- Pembersihan dan Pemrosesan Data: setelah data dapat diakses, dilakukan pembersihan diantaranya dilihat apakah ada data kosong, kesesuaian tipe data, dan data yang tidak relevan. 
- EDA : dilaukan analisis untuk memahami pola dan hubungan dalam data. Ini termasuk pembuatan visualisasi data, analisis statistik (disini lebih ditekankan menggunakan uji t-test (uji hipotesis mean dua populasi), dan identifikasi fitur-fitur yang akan digunakan untuk proses pemodelan. 
- Pemodelan: pembuatan model logistic regression melibatkan fitur-fitur yang sudah dipilih sebelumnya untuk dapat memprediksi attrition. 
- Evaluasi Model: dilakukan evaluasi model yang sudah dibuat menggunakan f1 score
- Deploy model : model yang sudah dibuat dan dievaluasi kemudian disimpan dan dipastikan dapat diakses untuk proses prediksi
- Pembuatan dashboard : untuk pemahaman yang lebih baik, dibuat dashboard dengan pertanyaan-pertanyaan yang mengarahkan pembaca untuk dapat memahami kondisi data terhadap nilai attrition. 

### Persiapan

Data : [clik here](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

```
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from scipy.stats import ttest_ind
from sklearn.linear_model import LogisticRegression
import pickle
```

## Business Dashboard

[click here for see dashboard](https://public.tableau.com/views/HRAttrition_17074180828750/HRAttrition?:language=en-US&:display_count=n&:origin=viz_share_link)

## Conclusion
Berdasarkan analisis yang sudah dilakukan dan pengujian dengan menggunakan uji t-test, maka diperoleh bahwa umur, durasi lama bekerja pada perusahaan, apakah karyawan mengalami over time atau tidak, pemasukan/gaji, level job, kepuasan lingkungan, dan kepuasan terhadap pekerjaan memiliki perbedaan yang signifikan pada karyawan yang mengalami attrition dan yang tidak. Contohnya pada segi umur, umur produktif (20an-30an) memiliki tingkat attrition rate tertinggi diantara umur lainnya. Juga karyawan dengan masa kerja tergolong masih baru (0-5 tahun) dan yang sudah sangat lama (31-40) memiliki attrition tertinggi, kemungkinan untuk karyawan pada 0-5  tahun, adalah masa untuk memastikan apakah pekerjaan sesuai atau tidak dengan passion yang dimiliki hingga adanya keinginan mencoba bidang pekerjaan lainnya. Sementara karyawan lama, dirasa sudah waktunya untuk masa pensiun. Sementara karyawan yang mengalami overtime dan yang tidak memiliki persentase yang cukup jauh dalam tingkat attrition rate, sebesar 23,56% dan 7,69%. Oleh karena itu, perusahaan dapat mempertimbangkan hal-hal ini untuk membuat kebijakan kedepannya pada perusahaan. 

### Rekomendasi Action Items 

Beberapa rekomendasi agar perusahaan Jaya Jaya Maju dapat mengurangi tingginya attrition rate pada karyawan yaitu : 

- Pengelolaan manajemen waktu kerja, seperti penerapan fleksibilitas jam kerja dan kebijakan cuti yang baik sesuai dengan kenyamanan para karyawan. Hal ini dapat lebih memudahkan sehingga memungkinkan lebih sedikit karyawan yang mengalami overtime.
- Insentif tersendiri sesuai dengan lamanya waktu kerja. Jika memungkinkan, jika diberi insentif khusus sesuai dengan masa kerja akan membuat karyawan lebih merasa betah bekerja dan untuk pemberian insentif bisa juga diberi periode tertentu misal 3 bulan sekali atau 6 
 bulan.
- Pengadaan acara untuk bonding antar karyawan. Meningkatkan hubungan antar karyawan dapat meningkatkan rasa kepedulian dan kebersamaan terhadap sesama karyawan dan hal ini juga berimbas pada kenyamanan dan kecintaan terhadap pekerjaan. Hal ini membuat karyawan lebih nyaman dan betah berkerja.  
