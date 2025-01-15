class BEMIter:
    """
    Base class for iterative BEM solvers.
    """
    
    def __init__(self, solver='gmres', tol=1e-4, maxit=200, restart=None, precond='hmat', output=0):
        self.solver = solver   # iterative solver, 'cgs', 'bicgstab', or 'gmres'
        self.tol = tol         # tolerance
        self.maxit = maxit     # maximum number of iterations
        self.restart = restart # restart for GMRES solver
        self.precond = precond # preconditioner for iterative solver
        self.output = output   # intermediate output for iterative solver
        
        # Protected properties
        self._flag = None      # flag from iterative routine
        self._relres = None    # relative residual error
        self._iter = None      # number of iterations
        self._eneisav = None   # previously computed wavelengths
        self._stat = None      # statistics for H-matrices
        self._timer = None     # timer statistics

    def info(self):
        """
        INFO - Get information for iterative solver.
        
        Usage for obj = BEMIter:
            obj.info()                            -  print statistics
            flag, relres, iter = obj.info()       -  get statistics
        
        Output:
            flag       :  convergence flag
            relres     :  relative residual norm
            iter       :  outer and inner iteration numbers
        """
        flag, relres, iter = self._flag, self._relres, self._iter
        
        if flag is None or relres is None or iter is None:
            return None
        
        if not hasattr(self, '_printstat'):
            raise NotImplementedError("The method '_printstat' is not implemented.")
        
        if not hasattr(self, '_output') or self._output == 0:
            for f, r, i in zip(flag, relres, iter):
                self._printstat(f, r, i)
        else:
            return flag, relres, iter

    def _printstat(self, flag, relres, iter):
        """
        Placeholder for the printstat method implementation.
        """
        print(f"Flag: {flag}, Relative Residual: {relres}, Iterations: {iter}")

# Example usage:
# bem_iter = BEMIter()
# bem_iter._flag = [0, 1]
# bem_iter._relres = [0.001, 0.002]
# bem_iter._iter = [(10, 5), (20, 10)]
# bem_iter.info()
# flag, relres, iter = bem_iter.info()
# print(flag, relres, iter)
