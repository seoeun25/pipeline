import kfp


def merge_csv(file_path: kfp.components.InputPath('Tarball'),
              output_csv: kfp.components.OutputPath('CSV')):
    import glob
    import pandas as pd
    import tarfile

    tarfile.open(name=file_path, mode="r|gz").extractall('data')
    df = pd.concat(
        [pd.read_csv(csv_file, header=None)
         for csv_file in glob.glob('data/*.csv')])
    df.to_csv(output_csv, index=False, header=False)

create_stemp_merge_csv = kfp.components.create_component_from_func(
    func=merge_csv,
    output_component_file='component.yaml',
    base_image='python:3.7',
    packages_to_install=['pandas==1.1.4']
)
