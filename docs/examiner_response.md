# Response to Supervisor Feedback — Prep for External Examiner

**Important framing before anything else:** a few of these points aren't really about
*wording* a better explanation — they're places where the write-up (`Silas.docx`)
describes something the actual code (repo) doesn't do, or reports numbers that
don't trace back to a completed, verifiable run. An external examiner who opens the
code after reading those claims will find the same gaps your supervisor did. For
those items, the "explainable answer" is: fix the artifact or the write-up before
defense, not just have better words ready. I've marked each point accordingly.

---

## 1. The "MobileNetV2-ViT" claim

**Supervisor's point:** No ViT was implemented; this is an unverified/fabricated claim.

**What's actually true:** Confirmed by direct inspection of the code — both stages
use a plain `tf.keras.applications.MobileNetV2` base (frozen, ImageNet weights) with
`GlobalAveragePooling2D → Dropout → Dense → output`. No attention layers, no
transformer blocks, no ViT implementation anywhere in `untitled8.py` / the notebook.
Yet the report's Chapter 4/5 text (lines ~1530, ~1605, ~1626 of the document) explicitly
describes a "hybrid MobileNetV2–Vision Transformer (ViT)" model.

**Status: needs correction, not defense.** This is not defensible to an examiner as
written. Your supervisor is right.

**Recommended action:** Remove every "ViT" / "hybrid Transformer" reference and
replace with an accurate description:
> "Both stages utilize a lightweight MobileNetV2 architecture pre-trained on
> ImageNet, with task-specific classification heads — a sigmoid output for Stage 1
> detection and a softmax output for Stage 2 fertility classification."

If an examiner asks why the abstract/conclusion mention ViT: the honest answer is
that it was an error in the write-up that has been corrected — not a design
decision to justify.

---

## 2. Dataset characterization

**Supervisor's point:** Missing source, labeling protocol, imaging conditions,
inclusion/exclusion criteria; corner-crop negatives aren't true negatives.

**What's actually true:** Your report's **Section 3.4.1** already contains most of
what was asked for — it's just not visible in the parts your supervisor may have
been reacting to:
- **Source**: "Chicken Egg Quality Analysis Dataset" by Kombe (2025) on Kaggle,
  collected at poultry sites in Bugesera and Nyagatare, Rwanda
- **Imaging setup**: fluorescent-bulb candling trays (20-egg capacity), IoT-enabled
  incubator prototype, incubation at 37.5–37.8°C / 55–60% RH
- **Inclusion/exclusion**: 5,700 collected → 4,275 retained after removing blurry/
  poorly-lit/inconsistent images (1,425 per class), then a 3,847-image subset used
  in this study

**One real gap to flag honestly:** the report says negative samples for Stage 1 came
from "Roboflow, supplemented with corner crops." **The actual code only does the
corner-crop generation — there's no Roboflow download step anywhere in the
notebook.** That line in the report doesn't match the implementation.

**Recommended action for the corner-crop critique itself:** your supervisor is
making a fair methodological point, and the honest answer to an examiner is not to
argue it away — corner-crops of egg images are not independent real-world non-egg
images (no kitchen counters, hands, other backgrounds). Acknowledge this directly:
> "The current negative-sample strategy is a limitation acknowledged in the study —
> synthetic corner crops teach the detector to reject partial/occluded egg views,
> but true out-of-distribution negatives (arbitrary background objects) were not
> included. This is listed as future work: sourcing genuine non-egg negatives."

And fix the Roboflow sentence — either actually add real Roboflow-sourced negatives
to the pipeline, or remove that claim from the write-up.

---

## 3. "Just a modified classification head" / no CBAM or architectural novelty

**Supervisor's point:** You need real architectural modification (e.g., CBAM), not
just a new head on a frozen backbone.

**What's actually true:** Confirmed — the backbone is used entirely frozen
(`base_model.trainable = False`); no CBAM, no attention modules, no architecture
diagrams with actual modifications exist in the code.

**Status: this is a legitimate scope critique, not a wording problem.**

**Honest answer for an examiner if you don't implement CBAM before defense:**
> "The current implementation prioritizes a lightweight, frozen-backbone transfer
> learning approach appropriate for low-resource farm deployment. Architectural
> enhancement via attention mechanisms (CBAM) was identified as a direction for
> future work rather than implemented in this iteration, given time and compute
> constraints."
This is a legitimate scoping defense — but only if the report doesn't simultaneously
claim CBAM (or the fictitious ViT) was used. It can't say both "frozen lightweight
backbone" and "hybrid attention architecture" — pick the true one.

**If you have time before defense:** I can help you actually implement CBAM as a
real module inserted into the MobileNetV2 feature maps — that would let you honestly
answer "yes" instead of falling back to the scope-limitation defense. Say the word
and I'll build it.

---

## 4. Epoch count / training procedure

**Supervisor's point:** 10 epochs is too small; use ≥30 with early stopping, and
document optimizer/LR schedule/regularization.

**What's actually true — and this is an internal inconsistency worth catching before
an examiner does:** The report (line ~1031) states training used *"early stopping
with a patience threshold of 30 epochs."* The actual notebook code sets
`epochs=5` for Stage 1, `epochs=10` for Stage 2, and `EarlyStopping(patience=5)`.
Patience=5 and epochs=30 are not the same thing, and neither matches what's written.

**Status: needs correction.** Whatever number you defend needs to be the number
actually used in a real, completed run — not a number that sounds more rigorous.

**Recommended action:** Re-run training with `epochs=30` (or more) and genuine
early stopping, using the corrected/reordered notebook from earlier in this
conversation, then update both the code defaults and the report to match the real
run. Document optimizer (Adam — already true), and add whatever LR schedule /
regularization you actually use (currently: Dropout 0.3/0.2, no LR schedule — either
add one and document it, or state plainly that a fixed learning rate was used and
why).

---

## 5. Missing metrics — mAP, ROC-AUC, inference latency

**Supervisor's point:** These are absent from the implementation.

**What's actually true, and this is the most serious item:** Chapter 3.7 of your own
report *lists* mAP, ROC-AUC, and Inference Latency as intended evaluation metrics.
Chapter 4.4 reports specific numbers — 98.4% / 96.7% accuracy, precision, recall,
F1 — for the *other* metrics, but never mAP, ROC-AUC, or latency. Beyond that: when
I reviewed the actual training notebook's execution history, **the cells that would
train and save the real models never finished running** (two upstream cells errored
with `NameError` before the imports/data ever loaded), and **the shipped `.h5`
"model" files in the repo are empty Git-LFS pointer stubs, not real trained
weights.**

**Status: this is the item to treat most carefully.** If the 98.4%/96.7%/F1-0.984
etc. numbers in Chapter 4 don't come from a completed, reproducible training run,
presenting them to an external examiner as measured results — rather than disclosing
they aren't yet backed by a verified run — is a real academic-integrity risk, not
just an incomplete-metrics issue. I'm flagging this directly because it's the one
place where "prepare a good answer" isn't the right frame; "generate the actual
numbers first" is.

**Recommended action, in order:**
1. Actually run the corrected, top-to-bottom notebook (already built earlier in
   this conversation) on the real dataset, end to end, so real weights get produced.
2. Compute mAP, ROC-AUC (with the actual curve), and measured inference latency
   from that real run — I can add these to the notebook's evaluation cells now if
   you want.
3. Replace the Chapter 4 numbers with whatever the real run actually produces —
   even if they're lower than what's currently written. A lower, real, defensible
   96% beats an unverifiable 98.4% every time in front of an examiner who can ask
   "show me the run that produced this."

---

## 6. "Justify each design decision with empirical evidence or literature support"

**What's actually true:** The report does cite real-sounding literature throughout
(Rahman et al. 2025, Irhebhude et al. 2025, Khairy & Candra 2025, etc.) for several
design choices (MobileNetV2 lightweight-ness, transfer learning generalization). I
haven't independently verified each citation's existence/accuracy — that's worth
doing yourself before defense, since a fabricated or misattributed citation is the
same category of problem as the ViT claim.

**Recommended action:** For each major design decision (backbone choice, two-stage
architecture, frozen weights, dropout rates), have one citation *and* one
empirical result ready — the empirical half only works once item 5 above is fixed.

---

## 7. Post-hoc Explainable AI (XAI / Grad-CAM)

**What's actually true:** Not implemented anywhere in the code. Your own literature
review (Chapter 2) cites Atwa et al. (2026) using Grad-CAM for a similar task —
so the report already knows what's expected, it just wasn't built.

**Status: legitimate gap, not a wording problem.**

**Honest answer if not implemented by defense:**
> "XAI integration (Grad-CAM-based visual explanations) was scoped as a
> stretch goal and is listed under future work, given the priority placed on
> completing and validating the core two-stage pipeline first."
Only usable if this is genuinely true and the classifier itself is real (see #5) —
an XAI overlay on top of a model that was never actually verified as trained
doesn't fix the underlying problem.

**If there's time:** Grad-CAM is a relatively small addition on top of a working
Keras model (few dozen lines) — I can build it once real weights exist.

---

## 8. Benchmarking against EfficientNet-Lite / SqueezeNet

**What's actually true:** Not present in the code — only MobileNetV2 was trained.

**Status: legitimate gap.**

**Honest answer:** Same pattern as #3 and #7 — either actually train 1–2 alternative
lightweight backbones and report a real comparison table (I can add this to the
notebook — it's a straightforward swap of `tf.keras.applications.MobileNetV2` for
`EfficientNetV2B0` / similar), or disclose it as future work rather than imply it
was done.

---

## 9. Redeployment after fixes

Once real weights exist (item 5), redeploying is mechanical: drop the new
`.h5` files + `label_mapping.json` into the app folder, replacing the current
LFS-pointer stubs, and the existing `app.py` / `ui_components.py` code will load
them without changes — that part of the system is already correctly wired up.

---

## Summary: what's defensible today vs. what needs work first

| Point | Defensible as-is? | Action needed |
|---|---|---|
| ViT claim | No | Remove/correct wording |
| Dataset source/imaging/criteria | Mostly yes | Fix the Roboflow-negatives sentence to match code |
| Corner-crop negatives | Defensible as acknowledged limitation | Add explicit limitation statement |
| CBAM / architectural novelty | No | Implement, or honestly scope as future work |
| Epoch count (30 vs 5/10) | No | Re-run with real epoch count, update report to match |
| mAP / ROC-AUC / latency / core accuracy numbers | **No — highest priority** | Run the fixed notebook end-to-end on real data, report only real results |
| Literature justification | Partially | Verify citations, pair with real empirical results |
| XAI | No | Implement or scope as future work |
| Benchmarking vs. other backbones | No | Implement or scope as future work |

The single highest-priority fix is #5 — everything else is defensible with either a
quick code fix or an honest "future work" framing, but presenting unverified
accuracy numbers as measured results is the one item that could turn a tough
supervisor review into a formal integrity problem with an external examiner. Want
me to start by running the real training end-to-end so the numbers in Chapter 4 are
genuine before you touch anything else?
