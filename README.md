# Egg Quality CNN — Two-Stage Detector + Fertility Classifier

Streamlit app that classifies chicken egg candling photos: Stage 1 checks
whether the image is an egg at all, Stage 2 (MobileNetV2 + CBAM) classifies
it as **fertile**, **infertile**, or **dead**.

## Repo layout

```
app.py                     Streamlit app entry point
ui_components.py           UI rendering + auth (reads credentials from st.secrets)
utils/
  preprocessing.py         Image preprocessing shared by app + training
  cbam.py                  Shared CBAM layer definition (needed to load the .h5 models)
egg_detector_final.h5      Stage 1 weights  <- add these; not committed by default, see below
fertility_classifier_final.h5  Stage 2 weights  <- add these
label_mapping.json          Real class-index mapping from the verified training run
requirements.txt
training/
  egg_analysis_cnn_full_training.ipynb   The corrected, CBAM/Grad-CAM/benchmark notebook
  legacy_untitled8.*                     Original notebook, kept for reference
docs/
  project_qa.md            Full Q&A on the system, extracted from code + report
  examiner_response.md     Response to supervisor feedback, point by point
results/
  metrics_summary.json     Real metrics from a completed training run
  confusion_matrix.png / roc_curves.png / accuracy_loss_curves.png
  backbone_benchmark.csv   MobileNetV2+CBAM vs EfficientNetV2B0 vs MobileNetV3Small
  labels_table.csv / stage1_detection.csv
.streamlit/
  secrets.toml.example     Template for login credentials — copy, fill in, never commit
```

## Setup

1. **Add the trained models.** Copy `egg_detector_final.h5` and
   `fertility_classifier_final.h5` (or the `_best` versions) from your Colab
   `OUTPUT_DIR` into the repo root, next to `app.py`.
2. **Set up credentials.** Copy `.streamlit/secrets.toml.example` to
   `.streamlit/secrets.toml`, fill in real usernames/passwords/roles. This
   file is git-ignored — it never gets committed.
3. **Install dependencies:** `pip install -r requirements.txt`
4. **Run locally:** `streamlit run app.py`

## Deploying via GitHub + Streamlit Community Cloud

1. `git lfs install` (once, locally) — `.h5` files are tracked via Git LFS
   (`.gitattributes` already configured).
2. `git add . && git commit -m "Real trained weights + CBAM/XAI upgrades" && git push`
3. Verify with `git lfs ls-files` that the `.h5` files show real byte sizes
   (megabytes), not ~133 bytes — that was the exact bug in the original repo.
4. Go to [share.streamlit.io](https://share.streamlit.io), sign in with
   GitHub, "New app" → pick this repo/branch → main file path `app.py`.
5. In the app's **Settings → Secrets**, paste the same content as your local
   `secrets.toml`.
6. Every subsequent `git push` to the connected branch auto-redeploys the
   live app — no manual redeploy step needed.

## Known limitations (documented, not hidden)

- Stage 1's negative samples are synthetic corner-crops of real egg images,
  not independent non-egg photos — see `docs/examiner_response.md` for the
  full discussion.
- The near-perfect Stage 2 metrics (99.84% accuracy) are real (see
  `results/metrics_summary.json`), but worth a one-line justification in
  any report/defense rather than presenting at face value — see
  `docs/examiner_response.md`.
