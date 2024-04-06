import numpy as np

def shift_invert_iteration(A, shift, num_iterations=100, tolerance=1e-6):
    n = A.shape[0]
    eigenvectors = np.eye(n)
    
    for _ in range(num_iterations):
        # Pergeseran Matrix 
        shifted_matrix = np.dot((np.linalg.inv(A - shift * np.eye(n))), A) #np.linalg.inv(A - shift * np.eye(n)) @ A
        
        # Metode QR untuk pergeseran matrix 
        Q, R = np.linalg.qr(shifted_matrix)
        
        # memperbarui nilai A dan eigenvectorn
        A = np.dot(R,Q) #R @ Q
        eigenvectors = np.dot(eigenvectors , Q) #eigenvectors @ Q
        
        # Mengecek konvergensi
        off_diagonal = np.sum(np.abs(A - np.diag(np.diag(A))))
        if off_diagonal < tolerance:
            break
    
    eigenvalues = np.diag(A)
    return eigenvalues, eigenvectors

# Definisikan matriks A
A = np.array([[4, 1, 0],
              [0, 2, 1],
              [0, 1, -1]])

# Pilih nilai pergeseran (shift)
shift_value = 10

# Hitung nilai eigen dan vektor eigen menggunakan metode pergeseran
eigenvalues, eigenvectors = shift_invert_iteration(A, shift_value)

# Cetak nilai eigen dan vektor eigen
print("Nilai Eigen:")
for eigenvalue in eigenvalues:
    print(eigenvalue)

print("\nVektor Eigen:")
for eigenvector in eigenvectors.T:
    print(eigenvector)