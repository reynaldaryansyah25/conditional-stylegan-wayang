# conditional-stylegan-wayang

## cara aktifkan .venv

    .venv\Scripts\Activate.ps1

conditional-stylegan-wayang/
│
├── data/
│ ├── raw/ # Dataset asli (labeled-indonesian-wayang)
│ ├── balanced/ # Hasil balancing per kelas (Wan)
│ │ ├── train/
│ │ └── val/
│ └── generated/ # Hasil generate per kelas (rey)
│
├── src/ # Semua .py (script utama)
│ ├── preprocessing/ # Script data & balancing (Wan)
│ │ ├── balance*dataset.py
│ │ ├── split_train_val.py
│ │ └── resize_images.py
│ │
│ ├── gan/ # Script training & generate (rey & Andri)
│ │ ├── train_conditional_stylegan.py
│ │ ├── generate_images.py
│ │ └── label_mapping.py
│ │
│ ├── evaluation/ # Script evaluasi kuantitatif (rey & Ahmad)
│ │ ├── compute_fid.py
│ │ └── collect_generated_for_eval.py
│ │
│ └── silhouettes/ # Script analisis siluet (Ahmad)
│ ├── extract_silhouettes.py
│ ├── shape_features.py
│ └── pca_silhouette.py
│
├── notebooks/ # Semua .ipynb untuk eksplorasi & analisis
│ ├── 01_dataset_overview.ipynb # Wan
│ ├── 02_training_logs_review.ipynb # rey & Andri
│ ├── 03_visual_eval_real_vs_gen.ipynb # rey
│ └── 04_silhouette_analysis.ipynb # Ahmad
│
├── models/ # Checkpoint GAN (Andri)
│ ├── baseline_128/
│ │ └── network-snapshot-*.pkl
│ └── main*256/
│ └── network-snapshot-*.pkl
│
├── results/ # Semua hasil untuk laporan
│ ├── samples_per_class/ # Grid gambar per tokoh (Anda)
│ ├── silhouettes/ # Hasil overlay & siluet (Ahmad)
│ ├── plots/ # Histogram, PCA, dll (Ahmad)
│ └── tables/ # Tabel FID, rekap data (Anda & Wan)
│
├── docs/ # Dokumen non-kode (semua)
│ ├── project_plan.md # Rencana kerja, timeline
│ ├── roles_and_tasks.md # Pembagian tugas per orang
│ └── methodology_notes.md # Catatan metodologi GAN & evaluasi
│
├── reports/ # Draft laporan & presentasi
│ ├── report_draft.docx
│ └── slides_presentation.pptx
│
├── README.md # Penjelasan repo (rey)
├── requirements.txt # Semua library Python
└── .gitignore
