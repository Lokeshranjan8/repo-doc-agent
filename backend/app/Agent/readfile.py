def read_file(repo, file_path: str):
    try:
        file_content = repo.get_contents(file_path)
        return file_content.decoded_content.decode("utf-8")
    except Exception as e:
        return f"Error reading file: {str(e)}"
