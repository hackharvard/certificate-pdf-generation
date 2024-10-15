# Certificate PDF Generation

You need a `input.csv` file with the following columns:
- `Project Name`
- `Hacker Name 1`
- `Hacker Name 2`
- `Hacker Name 3`
- `Hacker Name 4`

Run `python format_data.py` to generate the `players_per_row.csv` with the following columns:
- `Project Name`
- `Hacker Name`

Add a `cert.png` file (a high resolution PNG of the certificate) in the same directory as the script.


Run `python generate_certificates.py` to generate the PDF of the certificates as `certificates.pdf`.



