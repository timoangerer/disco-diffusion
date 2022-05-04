Example command:

    python gen_cli.py -m steps=250 n_batches=10 batch_name="Life" text_prompts='["The meaning of life, painting by Leonardo Da Vinci"]' +preview=

Note: Use the special command paramter `+preview=` to only print the job configuration.

Example command with parameter sweeping syntax:

    python gen_cli.py -m steps=250 n_batches=10 batch_name="Life" text_prompts='["The meaning of life, painting by ${sweep_prompt}"]' +preview=